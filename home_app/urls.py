from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

app_name = 'home_app'

urlpatterns = [
    path('', views.HomeView.as_view() , name='home_app'),
    # path('', cache_page(60*1)(views.HomeView.as_view()) , name='home_app'),
]