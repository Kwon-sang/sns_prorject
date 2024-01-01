from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth import login as auth_login

from .forms import UserSignupForm


login = LoginView.as_view(template_name='accounts/login_form.html')


def logout(request):
    messages.success(request, '로그아웃 하였습니다.')
    return logout_then_login(request)


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user=user)
            messages.success(request, '회원가입을 환영합니다.')
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = UserSignupForm()
    return render(request, 'accounts/signup_form.html', {'form': form})
