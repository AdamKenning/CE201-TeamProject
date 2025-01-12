from django.shortcuts import render, HttpResponse
from . models import TodoItem

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.
def home(request):          return render(request, "home.html")

def food(request):          return render(request, "tracking/food.html")
def diaper(request):        return render(request, "tracking/diaper.html")
def medication(request):    return render(request, "tracking/medication.html")
def growth(request):        return render(request, "tracking/growth.html")
def sleep(request):         return render(request, "tracking/sleep.html")
def emotion(request):       return render(request, "tracking/emotion.html")

# def login(request):         return render(request, "login.html")
def settings(request):      return render(request, "settings.html")


def dashboard(request):
    return render(request, "users/dashboard.html")

def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
    else:
        form = UserCreationForm()
    return render(request, "registration/sign_up.html", {"form": form})

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})