# Generated by Django 5.0.6 on 2024-06-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0005_alter_orderitem_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='color',
            field=models.CharField(max_length=50),
        ),
    ]
