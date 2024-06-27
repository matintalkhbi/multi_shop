from django.urls import path
from . import views


app_name = 'product_app'
urlpatterns = [
    path('<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('navbar' , views.NavBarPartialView.as_view(), name='navbar'),
    path('all', views.ProductListView.as_view(), name='product_list'),
]
