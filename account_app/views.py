from random import randint

from django.shortcuts import render, redirect, reverse
from django.views import View
from .models import LoginForm, RegisterForm, Otp, CheckOtpForm, User
from django.contrib.auth import authenticate, login, logout
from .sms import verification


# Create your views here.

# def login(request):
#     return render(request , template_name="account_app/login.html")

class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "account_app/login.html", {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                form.add_error('phone', 'Username or password is incorrect')
        else:
            form.add_error('phone', 'Username or password is incorrect')
        return render(request, "account_app/login.html", {'form': form})


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "account_app/register.html", {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            randcode = randint(1000,9999)
            cd = form.cleaned_data
            # SMS fix
            # SMS.verifications(randcode, cd)
            print(cd['phone'])
            verification(str(cd['phone']), str(randcode))
            Otp.objects.create(phone=cd['phone'] , code=randcode)

            return redirect(reverse('account_app:check_otp')+f'?phone={cd["phone"]}')

        else:
            form.add_error("phone", "invalid data")

        return render(request, "account_app/register.html", {'form': form})


class CheckOtpView(View):
    def get(self, request):
        form = CheckOtpForm()
        return render(request, "account_app/check_otp.html" , {'form': form})

    def post(self, request):
        phone = request.GET.get('phone')
        form = CheckOtpForm(request.POST)
        print('user is not true')
        if form.is_valid():
            cd = form.cleaned_data
            print('user')
            print(Otp.objects.all())
            print(phone)
            print(Otp.objects.filter(phone=phone))
            if Otp.objects.filter(code=cd['code'], phone=phone).exists():
                print('user is true')
                user = User.objects.create_user(phone=phone)
                login(request, user)
                return redirect("/")
        else:
            form.add_error("phone", "invalid data")
        return render(request, "account_app/check_otp.html" , {'form': form})