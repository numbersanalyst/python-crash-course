"""Defines the URL patterns for the users app."""
from django.urls import include, path
from django.contrib.auth import views as auth_views

from . import views

app_name = "users"
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("logout/", auth_views.LogoutView.as_view(template_name='users/logged_out.html'), name="logout"),
]

