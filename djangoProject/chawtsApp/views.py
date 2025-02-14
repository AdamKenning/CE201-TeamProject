from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.urls import reverse
from .forms import UserRegistrationForm, ProfileForm, ChildForm, ShareCodeForm, SleepLogForm, FoodLogForm, GrowthLogForm
from .models import Profile, FamilyAssociation, Child

from django.utils.safestring import mark_safe
import json

# tracking pages
@login_required
def food(request):
    selected_child = None
    if 'selected_child_id' in request.session:
        selected_child = Child.objects.filter(id=request.session['selected_child_id'], parents=request.user).first()

    if not selected_child:
        return redirect('dashboard')

    return render(request, "tracking/food.html", {
        "selected_child": selected_child,
    })

@login_required
def diaper(request):
    selected_child = None
    if 'selected_child_id' in request.session:
        selected_child = Child.objects.filter(id=request.session['selected_child_id'], parents=request.user).first()

    if not selected_child:
        return redirect('dashboard')

    return render(request, "tracking/diaper.html", {
        "selected_child": selected_child,
    })

@login_required
def medication(request):
    selected_child = None
    if 'selected_child_id' in request.session:
        selected_child = Child.objects.filter(id=request.session['selected_child_id'], parents=request.user).first()

    if not selected_child:
        return redirect('dashboard')

    return render(request, "tracking/medication.html", {
        "selected_child": selected_child,
    })

@login_required
def growth(request):
    selected_child = None
    if 'selected_child_id' in request.session:
        selected_child = Child.objects.filter(id=request.session['selected_child_id'], parents=request.user).first()

    if not selected_child:
        return redirect('dashboard')

    return render(request, "tracking/growth.html", {
        "selected_child": selected_child,
    })

@login_required
def sleep(request):
    selected_child = None
    if 'selected_child_id' in request.session:
        selected_child = Child.objects.filter(id=request.session['selected_child_id'], parents=request.user).first()

    if not selected_child:
        return redirect('dashboard')

    return render(request, "tracking/sleep.html", {
        "selected_child": selected_child,
    })

@login_required
def emotion(request):
    selected_child = None
    if 'selected_child_id' in request.session:
        selected_child = Child.objects.filter(id=request.session['selected_child_id'], parents=request.user).first()

    if not selected_child:
        return redirect('dashboard')

    return render(request, "tracking/emotion.html", {
        "selected_child": selected_child,
    })

# def login(request):         return render(request, "login.html")
def settings(request):
    return render(request, "management/settings.html")

@login_required
def select_child(request, child_id):
    #store child in session
    child = get_object_or_404(Child, id=child_id, parents=request.user)
    request.session['selected_child_id'] = child.id
    return redirect('dashboard')  # redirect back to start (refresh page)

def dashboard(request):
    if request.user.is_authenticated:
        selected_child = None
        if 'selected_child_id' in request.session:
            selected_child = Child.objects.filter(id=request.session['selected_child_id'], parents=request.user).first()

        children = request.user.children.all()

        # total logs per child
        log_counts = []
        for child in children:
            total_logs = (
                child.sleepLogs.count() +
                child.foodLogs.count() +
                child.growthLogs.count()
            )
            log_counts.append({
                "name": f"{child.firstName} {child.lastName}",
                "log_count": total_logs
            })

        # data for pie chart
        child_names = [child["name"] for child in log_counts]
        data_logs_per_child = [child["log_count"] for child in log_counts]

        # data for bar chart
        log_categories = ['Sleep', 'Food', 'Growth']
        log_category_counts = [
            sum(child.sleepLogs.count() for child in children),
            sum(child.foodLogs.count() for child in children),
            sum(child.growthLogs.count() for child in children),
        ]
    else:
        selected_child = None
        children = []
        child_names = []
        data_logs_per_child = []
        log_categories = []
        log_category_counts = []

    return render(request, "dashboard.html", {
            "selected_child": selected_child,
            "children": children,

            "child_names": json.dumps(child_names),
            "data_logs_per_child": json.dumps(data_logs_per_child),
            "log_categories": json.dumps(log_categories),
            "log_category_counts": json.dumps(log_category_counts),
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


# debug testing page
@login_required
def changeProfile(request):
    # Get or create the profile instance
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if profile_form.is_valid():
            profile_form.save()
            return redirect('changeProfile')

    else:
        profile_form = ProfileForm(instance=profile)

    return render(request, 'management/changeProfile.html', {
        'profile_form': profile_form,
    })

# child managing testing
@login_required
def createChild(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.save()
            child.shareCodeGenerate()

            # assign child to user
            FamilyAssociation.objects.create(parent=request.user, child=child, is_primary=True)

            return redirect('dashboard')
    else:
        form = ChildForm()

    return render(request, 'management/createChild.html', {'form': form})


@login_required
def addChild(request):
    if request.method == 'POST':
        form = ShareCodeForm(request.POST)

        if form.is_valid():
            code = form.cleaned_data['shareCode']

            try:
                child = Child.objects.get(shareCode=code)
            except Child.DoesNotExist:
                # code is invalid for a child
                return render(request, 'dashboard.html')


            # check sahre code is valid
            if code == child.shareCode:

                FamilyAssociation.objects.create(parent=request.user, child=child, is_primary=False)

                child.shareCodeGenerate()
                return redirect('dashboard')
            else:
                # reset sharecode to prevent guessing
                child.shareCodeGenerate()

                # go dashboard if code invalid
                return render(request, 'dashboard.html')
    else:
        form = ShareCodeForm()

    return render(request, 'management/addChild.html', {'form': form})

@login_required
def testing(request):
    selected_child = None
    if 'selected_child_id' in request.session:
        selected_child = Child.objects.filter(id=request.session['selected_child_id'], parents=request.user).first()

    if not selected_child:
        return redirect('dashboard')

    # forms
    sleep_log_form = SleepLogForm(request.POST or None)
    food_log_form = FoodLogForm(request.POST or None)
    growth_log_form = GrowthLogForm(request.POST or None)

    # form submissions
    if request.method == 'POST':
        if 'sleep_log' in request.POST and sleep_log_form.is_valid():
            sleep_log = sleep_log_form.save(commit=False)
            sleep_log.child = selected_child
            sleep_log.save()
            return redirect('testing')

        elif 'food_log' in request.POST and food_log_form.is_valid():
            food_log = food_log_form.save(commit=False)
            food_log.child = selected_child
            food_log.save()
            return redirect('testing')

        elif 'growth_log' in request.POST and growth_log_form.is_valid():
            growth_log = growth_log_form.save(commit=False)
            growth_log.child = selected_child
            growth_log.save()
            return redirect('testing')

    return render(request, "testing.html", {
        "selected_child": selected_child,
        "sleep_log_form": sleep_log_form,
        "food_log_form": food_log_form,
        "growth_log_form": growth_log_form,
    })

