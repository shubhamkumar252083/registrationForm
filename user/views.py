from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserDetails
from .forms import RegisterForm, LoginForm


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


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            objects = UserDetails.objects.filter(
                email=email).filter(password=password)
            if objects:
                return render(request, 'user.html', {"object": objects[0]})
        form = LoginForm()
        context = {
            'form': form,
            "msg": "please enter valid details"
        }
        return render(request, 'login.html', context)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def update_view(request, id):
    obj = get_object_or_404(UserDetails, id=id)
    form = RegisterForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "register.html", context)
