# Generated by Django 5.0.6 on 2024-06-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0006_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
