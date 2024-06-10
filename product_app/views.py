from django.shortcuts import render
from django.views.generic import ListView, DetailView

from product_app.models import Product


# Create your views here.


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
