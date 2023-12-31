from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import UserSignupForm


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, '회원가입을 환영합니다.')
            next_url = request.get('next', '/')
            return redirect(next_url)
    else:
        form = UserSignupForm()
    return render(request, 'accounts/signup_form.html', {'form': form})
