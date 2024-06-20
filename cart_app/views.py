from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from account_app.models import Address
from product_app.models import Product
from .cart_module import Cart
from .models import Order, OrderItem, DiscountCode
from django.conf import settings
import requests
import json
from account_app import sms

class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, "cart_app/cart_details.html", {'cart': cart})


class CartAddView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        size = request.POST.get('size', 'empty')
        color = request.POST.get('color', 'empty')
        quantity = request.POST.get('quantity')

        if product.size.all() and not size:
            return HttpResponseBadRequest("Size is required.")
        if product.color.all() and not color:
            return HttpResponseBadRequest("Color is required.")
        if not quantity or not quantity.isdigit() or int(quantity) <= 0:
            return HttpResponseBadRequest("Valid quantity is required.")

        cart = Cart(request)
        cart.add(product=product, size=size, color=color, quantity=int(quantity))  # Convert quantity to integer

        print('Product added:', {
            'product_id': product.id,
            'size': size,
            'color': color,
            'quantity': int(quantity),
        })

        return redirect("cart_app:cart_details")


class CartDeleteView(View):
    def get(self, request, pk):
        print(pk)
        cart = Cart(request)
        cart.delete(pk)
        return redirect("cart_app:cart_details")


class OrderDetailView(View):
    def get(self, request, id):
        order = get_object_or_404(Order, id=id)
        return render(request, 'cart_app/order_detail.html', {'order': order})


class OrderCreationView(View):
    def get(self, request):

        cart = Cart(request)
        order = Order.objects.create(user=request.user, total_price=cart.total())
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], color=item['color'], size=item['size'],
                                     quantity=item['quantity'], price=item['price'], discount=item['discount'])

            print('Order created:', {
                'order_id': order.id,
                'product': item['product'],
                'color': item['color'],
                'size': item['size'],
                'quantity': item['quantity'],
                'price': item['price'],
                # 'discount': item['discount']
            })
        #create a function for check the paid
        Cart.remove_cart(cart)

        return redirect('cart_app:order_details', order.id)


class ApplyDiscountView(View):
    def post(self, request, pk):
        code = request.POST.get('discount_code')
        order = get_object_or_404(Order, id=pk)

        if order.discount_code:
            messages.error(request, 'A discount code has already been applied to this order.')
            return redirect("cart_app:order_details", order.id)

        try:
            discount_code = DiscountCode.objects.get(name=code)
        except DiscountCode.DoesNotExist:
            messages.error(request, 'The discount code you entered does not exist.')
            return redirect("cart_app:order_details", order.id)

        if not discount_code.is_valid():
            messages.error(request, 'The discount code is either expired or no longer available.')
            return redirect("cart_app:order_details", order.id)

        # Save the original price before applying the discount
        if order.original_price == 0:
            order.original_price = order.total_price

        order.total_price = order.original_price - (order.original_price * discount_code.discount / 100)
        order.discount_code = discount_code
        order.save()

        discount_code.quantity -= 1
        discount_code.save()

        messages.success(request, 'Discount code applied successfully.')
        return redirect('cart_app:order_details', order.id)


class RemoveDiscountView(View):
    def post(self, request, pk):
        order = get_object_or_404(Order, id=pk)

        if order.discount_code:
            discount_code = order.discount_code
            order.total_price = order.original_price  # Reset to original price
            order.discount_code = None
            order.original_price = 0  # Clear the original price
            order.save()

            discount_code.quantity += 1
            discount_code.save()

            messages.success(request, 'Discount code removed successfully.')
        else:
            messages.error(request, 'No discount code to remove.')

        return redirect('cart_app:order_details', order.id)

class OrderPaidCompleted(View):
    def get(self,request):
        return render(request , 'cart_app/order_response.html')

sandbox = 'www'

ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = 'YOUR_PHONE_NUMBER'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/cart/verify/'

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views import View

from django.conf import settings
import json
import requests


class SendRequestView(View):
    def post(self, request, pk):
        order = get_object_or_404(Order, id=pk, user=request.user)
        address_id = request.POST.get('address')
        address = get_object_or_404(Address, id=address_id)

        order.address = f"Address: {address.address}, Postal_Code: {address.postal_code}, Phone: {address.phone}"
        order.is_paid = True
        order.save()

        request.session['order_id'] = str(order.id)

        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": order.total_price,
            "Description": "Order Payment",
            "Phone": request.user.phone,
            "CallbackURL": "http://yourcallbackurl.com/callback",
        }
        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}
        return redirect('cart_app:order_paid')


        # paid with zarin pal
        # try:
        #     response = requests.post("https://api.zarinpal.com/pg/v4/payment/request.json", data=data, headers=headers,
        #                              timeout=10)
        #
        #     if response.status_code == 200:
        #         response = response.json()
        #         if response['Status'] == 100:
        #             return HttpResponse(json.dumps(
        #                 {'status': True, 'url': "https://www.zarinpal.com/pg/StartPay/" + str(response['Authority']),
        #                  'authority': response['Authority']}), content_type="application/json")
        #         else:
        #             return HttpResponse(json.dumps({'status': False, 'code': str(response['Status'])}),
        #                                 content_type="application/json")
        #     return HttpResponse(json.dumps(response), content_type="application/json")
        #
        # except requests.exceptions.Timeout:
        #     return HttpResponse(json.dumps({'status': False, 'code': 'timeout'}), content_type="application/json")
        # except requests.exceptions.ConnectionError:
        #     return HttpResponse(json.dumps({'status': False, 'code': 'connection error'}),
        #                         content_type="application/json")


class VerifyView(View):
    def get(self, request, pk):
        order_id = request.session.get('order_id')
        order = Order.objects.get(id=int(order_id))
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": amount,

        }

        data = json.dumps(data)
        # set content length by data
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}
        response = requests.post(ZP_API_VERIFY, data=data, headers=headers)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                order.is_paid = True
                order.save()
                # sms.SendSMS(order.user.phone , order.total_price)
                return {'status': True, 'RefID': response['RefID']}
            else:
                return {'status': False, 'code': str(response['Status'])}
        return response