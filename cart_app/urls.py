from django.urls import path

from . import views

app_name = 'cart_app'

urlpatterns = [
    path('details', views.CartDetailView.as_view(), name='cart_details'),
    path('add/<int:pk>', views.CartAddView.as_view(), name='cart_add'),
    path('delete/<str:pk>', views.CartDeleteView.as_view(), name='cart_delete'),
    path('order/<int:id>' , views.OrderDetailView.as_view(), name='order_details'),
    path('order/add', views.OrderCreationView.as_view(), name='order_creation'),
    path('apply-discount/<int:pk>/', views.ApplyDiscountView.as_view(), name='apply_discount'),
    path('remove-discount/<int:pk>/', views.RemoveDiscountView.as_view(), name='remove_discount'),
    path('sendrequest/<int:pk>/', views.SendRequestView.as_view(), name='send_request'),
    path('verify',views.VerifyView.as_view(), name='verify_request'),
    path('orderpaid' , views.OrderPaidCompleted.as_view(), name='order_paid'),
]