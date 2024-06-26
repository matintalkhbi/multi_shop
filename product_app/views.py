from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView

from product_app.models import Product,Category


# Create your views here.


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class NavBarPartialView(TemplateView):
    template_name = "includes/navbar.html"

    def get_context_data(self, **kwargs):
        context = super(NavBarPartialView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context
