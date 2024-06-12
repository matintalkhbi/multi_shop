from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseBadRequest
from product_app.models import Product
from .cart_module import Cart
from .models import Order, OrderItem


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
            'quantity': int(quantity)
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
            OrderItem.objects.create(order=order, product=item['product'], color=item['color'], size=item['size'][0],
                                     quantity=item['quantity'], price=item['price'])
            print('Order created:', {
                'order_id': order.id,
                'product': item['product'],
                'color': item['color'],
                'size': item['size'],
                'quantity': item['quantity'],
                'price': item['price']
            })
        return redirect('cart_app:order_details', order.id)
