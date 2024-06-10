from django.urls import path

from . import views

app_name = 'cart_app'

urlpatterns = [
    path('details', views.CartDetailView.as_view(), name='cart_details'),
    path('add/<int:pk>', views.CartAddView.as_view(), name='cart_add'),
]