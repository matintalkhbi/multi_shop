# Generated by Django 5.0.6 on 2024-06-06 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0006_otp_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otp',
            name='token',
        ),
    ]
