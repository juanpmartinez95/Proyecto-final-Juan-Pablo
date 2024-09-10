from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm, CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from .models import Usuario
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm 


def home(request):
    return render(request, 'core/index.html')



def sobre_mi(request):
    return render(request, 'core/sobre_mi.html')


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Usuario creado exitosamente.")
            print("Profile picture:", user.profile_pic)  
            return redirect('core:home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"

    def get_success_url(self):
        return reverse_lazy('core:home')


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente!")
            return redirect('core:home')
    else:
        form = CustomUserChangeForm(instance=request.user)
        
    return render(request, 'core/edit_profile.html', {'form': form})