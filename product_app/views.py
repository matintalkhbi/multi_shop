from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from product_app.models import Product, Category, Color, Size

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class NavBarPartialView(TemplateView):
    template_name = "includes/navbar.html"

    def get_context_data(self, **kwargs):
        context = super(NavBarPartialView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class ProductListView(ListView):
    template_name = "product_list.html"
    context_object_name = 'product_list'
    paginate_by = 9  # تعداد آیتم‌ها در هر صفحه

    def get_queryset(self):
        sizes = self.request.GET.getlist('size')
        colors = self.request.GET.getlist('color')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        queryset = Product.objects.all()

        if colors:
            queryset = queryset.filter(color__id__in=colors).distinct()
        if sizes:
            queryset = queryset.filter(size__id__in=sizes).distinct()
        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['colors'] = Color.objects.all()
        context['sizes'] = Size.objects.all()
        context['selected_colors'] = self.request.GET.getlist('color')
        context['selected_sizes'] = self.request.GET.getlist('size')
        context['min_price'] = self.request.GET.get('min_price')
        context['max_price'] = self.request.GET.get('max_price')
        return context
