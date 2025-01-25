from django.shortcuts import render, HttpResponse

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import UserRegistrationForm, ProfileForm
from .models import Profile



# Create your views here.
def home(request):
    profile = request.user.profile
    if not profile.profile_picture:
        profile_picture_url = '/static/images/default-profile-picture.jpg'
    else:
        profile_picture_url = profile.profile_picture.url

    return render(request, 'home.html', {'profile_picture_url': profile_picture_url})

def food(request):          return render(request, "tracking/food.html")
def diaper(request):        return render(request, "tracking/diaper.html")
def medication(request):    return render(request, "tracking/medication.html")
def growth(request):        return render(request, "tracking/growth.html")
def sleep(request):         return render(request, "tracking/sleep.html")
def emotion(request):       return render(request, "tracking/emotion.html")

# def login(request):         return render(request, "login.html")
def settings(request):      return render(request, "settings.html")


def dashboard(request):
    return render(request, "registration/dashboard.html")

# def sign_up(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect(reverse("dashboard"))
#     else:
#         form = UserCreationForm()
#     return render(request, "registration/sign_up.html", {
#         "form": form
#         })

def sign_up(request):
    if request.method == "POST":

        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            # Save the user
            user = user_form.save()

            # Create / update the profile
            profile, created = Profile.objects.get_or_create(user=user)

            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()


            # Log the user in
            login(request, user)
            return redirect('dashboard')

    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()

    return render(request, 'registration/sign_up.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        })
