# Generated by Django 5.0.6 on 2024-06-09 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0002_alter_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='product_app.color'),
        ),
    ]
