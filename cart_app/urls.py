from django.urls import path

from . import views

app_name = 'cart_app'

urlpatterns = [
    path('details', views.CartView.as_view(), name='cart_details'),
]