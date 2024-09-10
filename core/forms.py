from django  import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import Usuario

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ["username", "password"]
        widget = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'profile_pic']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
        }
class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = Usuario
        fields = ['username', 'profile_pic']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
        }