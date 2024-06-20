from django.db import models
from account_app.models import User
from product_app.models import Product, Size, Color
from django.utils import timezone

class DiscountCode(models.Model):
    name = models.CharField(max_length=50, unique=True)
    discount = models.SmallIntegerField(default=0)
    quantity = models.SmallIntegerField(default=1)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def is_valid(self):
        now = timezone.now()
        if self.start_date and self.end_date:
            return self.start_date <= now <= self.end_date and self.quantity > 0
        elif self.start_date:
            return self.start_date <= now and self.quantity > 0
        elif self.end_date:
            return now <= self.end_date and self.quantity > 0
        else:
            return self.quantity > 0

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_price = models.IntegerField(default=0)
    original_price = models.IntegerField(default=0)  # Added field for storing original price
    created = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    address_link = models.URLField(blank=True, null=True)
    discount_code = models.ForeignKey(DiscountCode, null=True, blank=True, on_delete=models.SET_NULL, related_name='orders')

    def __str__(self):
        return self.user.username



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



