from django.db import models

# Create your models here.


class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    # category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.SmallIntegerField()
    discount = models.SmallIntegerField()
    image = models.ImageField(upload_to='products/')
    size = models.ManyToManyField(Size, related_name='products', blank=True , null=True)
    color = models.ManyToManyField(Color, related_name='products', blank=True , null=True)


    def __str__(self):
        return self.title


class Information(models.Model):
    product = models.ForeignKey(Product,null=True ,blank=True, on_delete=models.CASCADE, related_name='information')
    text = models.TextField()

    def __str__(self):
        return self.text

