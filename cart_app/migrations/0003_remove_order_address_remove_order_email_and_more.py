# Generated by Django 5.0.6 on 2024-06-11 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0002_rename_qunatity_orderitem_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
    ]
