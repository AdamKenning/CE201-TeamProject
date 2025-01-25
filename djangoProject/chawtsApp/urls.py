from django.urls import path, include
from django.shortcuts import redirect
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", lambda request: redirect("home/", permanent=False)),

    path("food/",       views.food,         name = "food"),
    path("diaper/",     views.diaper,       name = "diaper"),
    path("medication/", views.medication,   name = "medication"),
    path("growth/",     views.growth,       name = "growth"),
    path("sleep/",      views.sleep,        name = "sleep"),
    path("emotion/",    views.emotion,      name = "emotion"),

    path("home/",       views.home,         name = "home"),
    path("settings/",   views.settings,     name = "settings"),

    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("sign_up/", views.sign_up, name="sign_up"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # for profile pictures