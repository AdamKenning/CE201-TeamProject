from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import UserRegistrationForm, ProfileForm
from .models import Profile

# tracking pages
def food(request):          return render(request, "tracking/food.html")
def diaper(request):        return render(request, "tracking/diaper.html")
def medication(request):    return render(request, "tracking/medication.html")
def growth(request):        return render(request, "tracking/growth.html")
def sleep(request):         return render(request, "tracking/sleep.html")
def emotion(request):       return render(request, "tracking/emotion.html")

# misc
def home(request):          return render(request, 'home.html')

# def login(request):         return render(request, "login.html")
def settings(request):      return render(request, "settings.html")


def dashboard(request):
    return render(request, "registration/dashboard.html")


# debug testing page
@login_required
def testing(request):
    # Get or create the profile instance
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if profile_form.is_valid():
            profile_form.save()
            return redirect('testing')

    else:
        profile_form = ProfileForm(instance=profile)

    return render(request, 'testing.html', {
        'profile_form': profile_form,
    })

def sign_up(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
    else:
        user_form = UserRegistrationForm()
    return render(request, "registration/sign_up.html", {
        "user_form": user_form
        })