from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserDetails
from .forms import RegisterForm
import os
from django.conf import settings


def home_view(request):
    return render(request, "home.html")


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = RegisterForm()
            return render(request, 'register.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
