from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    def clean_email(self):
        if email := self.cleaned_data.get('email'):
            if User.objects.filter(email=email):
                raise forms.ValidationError('이미 등록된 이메일 입니다.')

