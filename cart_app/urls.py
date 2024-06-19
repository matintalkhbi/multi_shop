from django.urls import path

from . import views

app_name = 'cart_app'

urlpatterns = [
    path('details', views.CartDetailView.as_view(), name='cart_details'),
    path('add/<int:pk>', views.CartAddView.as_view(), name='cart_add'),
    path('delete/<str:pk>', views.CartDeleteView.as_view(), name='cart_delete'),
    path('order/<int:id>' , views.OrderDetailView.as_view(), name='order_details'),
    path('order/add', views.OrderCreationView.as_view(), name='order_creation'),
    path('applydiscount/<int:pk>', views.ApplyDiscountView.as_view(), name='apply_discount'),
]