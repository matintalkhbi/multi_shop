# Generated by Django 5.0.6 on 2024-06-20 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0011_order_discount_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_price',
            field=models.IntegerField(default=0),
        ),
    ]
