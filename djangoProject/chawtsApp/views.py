from django.shortcuts import render, HttpResponse
from . models import TodoItem

# Create your views here.
def food(request):          return render(request, "food.html")
def diaper(request):        return render(request, "diaper.html")
def medication(request):    return render(request, "medication.html")
def home(request):          return render(request, "home.html")
def growth(request):        return render(request, "growth.html")
def sleep(request):         return render(request, "sleep.html")
def emotion(request):       return render(request, "emotion.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})