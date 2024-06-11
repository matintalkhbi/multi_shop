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
            item['total'] = int(item['price']) * int(item['quantity'])
            item['unique_id'] = self.unique_id_generator(product.id , item['color'] , item['size'])
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
                'id': str(product.id)
            }
        self.cart[unique]['quantity'] += int(quantity)  # Ensure quantity is an integer
        self.save()

    def delete(self, id):
        if id in self.cart:
            del self.cart[id]
            self.save()


    def save(self):
        self.session[CART_SESSION_ID] = self.cart
        self.session.modified = True
