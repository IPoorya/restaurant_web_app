from django.shortcuts import redirect, render
from django.views import View
from django. contrib import messages
import random
from .forms import UserCreationForm, VerifyCodeForm, loginForm
from .models import User, Otpcode
from utils import send_otp_code
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


class signup(View):
    form_class = UserCreationForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/signup.html', {
            'form': form,
        })

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(10000, 99999)
            send_otp_code(form.cleaned_data['phone_number'], random_code)
            Otpcode.objects.create(
                phone_number=form.cleaned_data['phone_number'], code=random_code)
            request.session['user_signup_info'] = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'phone_number': form.cleaned_data['phone_number'],
                'password': form.cleaned_data['password2'],
                'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            }
            return redirect('accounts:verify_code')
        return render(request, 'accounts/signup.html', {
            'form': form,
        })


class verifyCodeView(View):
    form_class = VerifyCodeForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/verify_code.html', {
            'form': form,
        })

    def post(self, request):
        form = self.form_class(request.POST)
        user_session = request.session['user_signup_info']
        if form.is_valid():
            db_code = Otpcode.objects.filter(
                created_at=user_session['created_at'], phone_number=user_session['phone_number'])
            user_code = form.cleaned_data['code']

            if db_code and db_code[0].is_expired:
                messages.error(
                    request, 'your code has been expired', 'danger')
                return render(request, 'accounts/verify_code.html', {
                    'form': form,
                })

            if db_code and db_code[0].code == user_code:
                messages.success(
                    request, 'you signed up successfully', 'success')
                user = User.objects.create_user(name=user_session['name'],
                                                email=user_session['email'],
                                                phone_number=user_session['phone_number'],
                                                password=user_session['password'])
                login(request, user)
                return redirect('home:home')

            messages.error(request, 'wrong code', 'danger')
            return render(request, 'accounts/verify_code.html', {
                'form': form,
            })


class loginView(View):
    form_class = loginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/login.html', {
            'form': form,
        })

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            messages.success(request, 'logged in successfully', 'success')
            user = authenticate(
                request, username=form.cleaned_data['phone_number'], password=form.cleaned_data['password'])
            print(user)
            if user is not None:
                login(request, user)
            return redirect('home:home')
        return render(request, 'accounts/login.html', {
            'form': form,
        })


class logoutView(LoginRequiredMixin, View):
    redirect_field_name = "home:home"

    def get(self, request):
        logout(request)
        return redirect('home:home')
