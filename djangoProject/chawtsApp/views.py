from django.shortcuts import render, HttpResponse
from . models import TodoItem

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.
def food(request):          return render(request, "food.html")
def diaper(request):        return render(request, "diaper.html")
def medication(request):    return render(request, "medication.html")
def home(request):          return render(request, "home.html")
def growth(request):        return render(request, "growth.html")
def sleep(request):         return render(request, "sleep.html")
def emotion(request):       return render(request, "emotion.html")

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