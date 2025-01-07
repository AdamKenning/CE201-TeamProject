from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path("", lambda request: redirect("home/", permanent=False)),

    path("food/",       views.food,         name = "food"),
    path("diaper/",     views.diaper,       name = "diaper"),
    path("medication/", views.medication,   name = "medication"),
    path("home/",       views.home,         name = "home"),
    path("growth/",     views.growth,       name = "growth"),
    path("sleep/",      views.sleep,        name = "sleep"),
    path("emotion/",    views.emotion,      name = "emotion"),
    

    path("todos/", views.todos, name = "todos"),
]