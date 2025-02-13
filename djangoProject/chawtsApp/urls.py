from django.urls import path, include
from django.shortcuts import redirect
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # empty url redirects to home page
    path("", lambda request: redirect("dashboard/", permanent=False)),

    # user login stuff / accounting
    path("accounts/", include("django.contrib.auth.urls")),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("changeProfile/",    views.changeProfile,      name = "changeProfile"),

    # home page
    path("dashboard/", views.dashboard, name="dashboard"),

    # childManagement pages
    path('createChild/', views.createChild, name='createChild'),
    path('addChild/', views.addChild, name='addChild'),
    path('select-child/<int:child_id>/', views.select_child, name='select_child'),  # Add this!

    # tracking pages
    path("food/",       views.food,         name = "food"),
    path("diaper/",     views.diaper,       name = "diaper"),
    path("medication/", views.medication,   name = "medication"),
    path("growth/",     views.growth,       name = "growth"),
    path("sleep/",      views.sleep,        name = "sleep"),
    path("emotion/",    views.emotion,      name = "emotion"),

    # misc
    path("settings/",   views.settings,     name = "settings"),

    # testing page
    path("testing/",    views.testing,      name = "testing"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # for profile pictures