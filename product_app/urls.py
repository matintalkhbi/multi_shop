from django.urls import path
from .views import ProductDetailView, NavBarPartialView, ProductListView

app_name = 'product_app'
urlpatterns = [
    path('<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('navbar', NavBarPartialView.as_view(), name='navbar'),
    path('all', ProductListView.as_view(), name='product_list'),
]
