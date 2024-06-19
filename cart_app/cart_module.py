from product_app.models import Product

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if cart is None:
            cart = self.session[CART_SESSION_ID] = {}
        elif isinstance(cart, list):
            cart = self.session[CART_SESSION_ID] = {}  # Reset to empty dict if it was a list
        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()
        for item in cart.values():
            product = Product.objects.get(pk=int(item['id']))
            item['product'] = Product.objects.get(pk=int(item['id']))
            item['total'] = int(item['price']) * int(item['quantity']) * (100 - (int(item['discount']) ))/100
            print(item['total'])
            item['unique_id'] = self.unique_id_generator(product.id, item['color'], item['size'])
            yield item

    def unique_id_generator(self, id, color, size):
        return f'{id}-{color}-{size}'

    def add(self, product, color, size, quantity):
        unique = self.unique_id_generator(product.id, color, size)
        if unique not in self.cart:
            self.cart[unique] = {
                'quantity': 0,
                'price': str(product.price),
                'color': color,
                'size': size,
                'id': str(product.id),
                'discount': int(product.discount),
            }
        self.cart[unique]['quantity'] += int(quantity)
        self.save()

    def delete(self, id):
        if id in self.cart:
            del self.cart[id]
            self.save()

    def total(self):
        cart = self.cart.values()

        total = sum(int(item['price']) * int(item['quantity']) * (100 - (int(item['discount']) ))/100 for item in cart)
        return total

    def save(self):
        self.session[CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove_cart(self):
        del self.session[CART_SESSION_ID]
