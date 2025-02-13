from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.urls import reverse
from .forms import UserRegistrationForm, ProfileForm, ChildForm, ShareCodeForm, SleepLogForm, FoodLogForm, GrowthLogForm
from .models import Profile, FamilyAssociation, Child, SleepLog, FoodLog, GrowthLog



# tracking pages
def food(request):          return render(request, "tracking/food.html")
def diaper(request):        return render(request, "tracking/diaper.html")
def medication(request):    return render(request, "tracking/medication.html")
def growth(request):        return render(request, "tracking/growth.html")
def sleep(request):         return render(request, "tracking/sleep.html")
def emotion(request):       return render(request, "tracking/emotion.html")


# def login(request):         return render(request, "login.html")
def settings(request):      return render(request, "settings.html")

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
    else:
        children = []
        selected_child = None

    return render(request, "dashboard.html", {
        "selected_child": selected_child,
        "children": children,
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

    return render(request, 'profileManagement/changeProfile.html', {
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

    return render(request, 'childManagement/createChild.html', {'form': form})


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

    return render(request, 'childManagement/addChild.html', {'form': form})

