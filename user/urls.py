from django.urls import path
from .views import *
urlpatterns = [
    path("", home_view, name="home_view"),
    path("register/", register_view, name="register_view"),
    path("login/", login_view, name="login_view"),
]
