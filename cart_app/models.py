from django.db import models
from account_app.models import User
from product_app.models import Product, Size, Color




class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_price = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.phone

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    # problem : سایز و رنگ چون مستقیم به مدل خودشون وصل هستن توی دو تا استرینگ قرار می  گیرن : size and color => models size and color
    # size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='items')
    size = models.CharField(max_length=50)
    # color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='items')
    color = models.CharField(max_length=50)
    discount = models.SmallIntegerField(default=0)
    quantity = models.SmallIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    def total_price(self):
        price = self.price * self.quantity
        discount = (100 - self.discount)/100
        return price * discount

    def __str__(self):
        return self.order.user.phone


class DiscountCode(models.Model):
    name = models.CharField(max_length=50 , unique=True)
    discount = models.SmallIntegerField(default=0)
    quantity = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.name
