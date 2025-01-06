from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path("", lambda request: redirect("home/", permanent=False)),
    path("home/", views.home, name = "home"),
    path("todos/", views.todos, name = "todos"),
]