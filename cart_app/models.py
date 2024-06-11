from django.db import models
from account_app.models import User
from product_app.models import Product, Size, Color

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    address = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.phone

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='items')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='items')
    quantity = models.SmallIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.order.phone
