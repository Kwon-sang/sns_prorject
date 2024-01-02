from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, logout_then_login, PasswordChangeView
from django.contrib.auth import login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .forms import UserSignupForm, UserProfileEditForm


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


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('login')
    template_name = 'accounts/password_change_form.html'

    def form_valid(self, form):
        messages.success(self.request, '비밀번호가 변경되었습니다.')
        return super().form_valid(form)


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserProfileEditForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '프로필 정보를 수정 하였습니다.')
            return redirect('profile_edit')
    else:
        form = UserProfileEditForm(instance=request.user)
    return render(request, 'accounts/profile_edit_form.html', {'form': form})
