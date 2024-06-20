from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseBadRequest
from product_app.models import Product
from .cart_module import Cart
from .models import Order, OrderItem, DiscountCode
from django.conf import settings
import requests
import json

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
        Cart.remove_cart(cart)
        return redirect('cart_app:order_details', order.id)


# class ApplyDiscountView(View):
#     def post(self, request, pk):
#         code = request.POST.get('discount_code')
#         order = get_object_or_404(Order, id=pk)
#         discount_code = get_object_or_404(DiscountCode, name=code)
#         print(discount_code)
#         if discount_code.quantity == 0:
#             return redirect("cart_app:order_details", order.id)
#         order.total_price -= order.total_price * discount_code.discount / 100
#         order.save()
#         discount_code.quantity -= 1
#         discount_code.save()
#         return redirect('cart_app:order_details', order.id)

from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .models import Order, DiscountCode

class ApplyDiscountView(View):
    def post(self, request, pk):
        code = request.POST.get('discount_code')
        order = get_object_or_404(Order, id=pk)

        if order.discount_code:
            # اضافه کردن پیام خطا
            messages.error(request, 'A discount code has already been applied to this order.')
            return redirect("cart_app:order_details", order.id)

        discount_code = get_object_or_404(DiscountCode, name=code)

        if discount_code.quantity == 0:
            messages.error(request, 'This discount code is no longer available.')
            return redirect("cart_app:order_details", order.id)

        order.total_price -= order.total_price * discount_code.discount / 100
        order.discount_code = discount_code
        order.save()

        discount_code.quantity -= 1
        discount_code.save()

        messages.success(request, 'Discount code applied successfully.')
        return redirect('cart_app:order_details', order.id)







sandbox = 'www'

ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = 'YOUR_PHONE_NUMBER'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/cart/verify/'


class SendRequestView(View):
    def post(self, request , pk):
        order = get_object_or_404(Order, id=pk , user=request.user)
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": order.total_price,
            "Description": description,
            "Phone": request.user.phone,
            "CallbackURL": CallbackURL,

        }
        data = json.dumps(data)
        # set content length by data
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}
        try:
            response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)

            if response.status_code == 200:
                response = response.json()
                if response['Status'] == 100:
                    return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']),
                            'authority': response['Authority']}
                else:
                    return {'status': False, 'code': str(response['Status'])}
            return response

        except requests.exceptions.Timeout:
            return {'status': False, 'code': 'timeout'}
        except requests.exceptions.ConnectionError:
            return {'status': False, 'code': 'connection error'}
