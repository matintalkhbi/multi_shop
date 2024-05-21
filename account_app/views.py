from django.shortcuts import render
from django.views import View
from .models import LoginForm
# Create your views here.

# def login(request):
#     return render(request , template_name="account_app/login.html")

class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "account_app/login.html", {'form': form})