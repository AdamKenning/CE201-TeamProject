from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from datetime import date
from .forms import *
from .models import *

# for pdf export
from reportlab.pdfgen import canvas
from django.http import FileResponse, HttpResponseRedirect
from django.urls import reverse

from django.utils.safestring import mark_safe
import json

# dashboard
def dashboard(request):
    if request.user.is_authenticated:
        selected_child = None
        is_primary = False;
        age_years = None
        age_months = None
        if 'selected_child_id' in request.session:
            selected_child = Child.objects.filter(id=request.session['selected_child_id'], parents=request.user).first()
            is_primary = FamilyAssociation.objects.filter(
                    parent=request.user,
                    child=selected_child,
                    is_primary=True
                ).exists()
            age_days_total = (date.today() - selected_child.dateOfBirth).days
            age_years = age_days_total // 365
            age_months = (age_days_total - (age_years * 365)) // 30


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
        is_primary = False
        age_years = None
        age_months = None
        children = []
        child_names = []


        data_logs_per_child = []
        log_categories = []
        log_category_counts = []

    return render(request, "dashboard.html", {
            "selected_child": selected_child,
            "is_primary": is_primary,
            "selected_child_years": age_years,
            "selected_child_months": age_months,
            "children": children,

            "child_names": json.dumps(child_names),
            "data_logs_per_child": json.dumps(data_logs_per_child),
            "log_categories": json.dumps(log_categories),
            "log_category_counts": json.dumps(log_category_counts),
        })

# registration page
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

# tracking pages
@login_required
def food(request):

    selected_child = None
    if 'selected_child_id' in request.session:
        selected_child = Child.objects.filter(id=request.session['selected_child_id'], parents=request.user).first()

    if not selected_child:
        return redirect('dashboard')
    if request.method == "POST":
        form = FoodLogForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.child = selected_child
            meal.save()
            return redirect('food')

    meals = FoodLog.objects.filter(child=selected_child).order_by('-timeEvent')

    chart_data = {
        "labels": [meal.timeEvent.strftime('%Y-%m-%d %H:%M') for meal in meals],
        "calories": [meal.calories for meal in meals]
    }

    return render(request, "tracking/food.html", {
        "selected_child": selected_child,
        "meals": meals,
        "chart_data": json.dumps(chart_data),
    })
'''
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
'''
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
'''
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
'''
# misc management pages
@login_required
def settings(request):
    return render(request, "management/settings.html")

@login_required
def select_child(request, child_id):
    #store child in session
    child = get_object_or_404(Child, id=child_id, parents=request.user)
    request.session['selected_child_id'] = child.id
    return redirect('dashboard') # refresh page

@login_required
def deselect_child(request):
    if 'selected_child_id' in request.session:
        del request.session['selected_child_id']  # delete session
    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))  # Redirect back or to dashboard

# child managing testing
@login_required
def createChild(request):
    if request.method == 'POST':
        form = ChildForm(request.POST, request.FILES)
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


            # check share code is valid
            if code == child.shareCode:

                FamilyAssociation.objects.create(parent=request.user, child=child, is_primary=False)

                child.shareCodeGenerate()
                return redirect('dashboard')
            else:
                # reset share code to prevent guessing
                child.shareCodeGenerate()

                # go dashboard if code invalid
                return render(request, 'dashboard.html')
    else:
        form = ShareCodeForm()

    return render(request, 'management/addChild.html', {'form': form})

@login_required
def edit_child(request):
    selected_child = None
    is_primary = False
    if 'selected_child_id' in request.session:
        selected_child = Child.objects.filter(id=request.session['selected_child_id'], parents=request.user).first()
        is_primary = FamilyAssociation.objects.filter(
                    parent=request.user,
                    child=selected_child,
                    is_primary=True
                ).exists()
    else:
        return redirect('dashboard')

    if(is_primary == False):
       return redirect('dashboard')

    if request.method == "POST":
        form = ChildEditForm(request.POST, request.FILES, instance=selected_child)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ChildEditForm(instance=selected_child)

    return render(request, 'management/edit_child.html', {'form': form, 'selected_child': selected_child})


@login_required
def changeProfile(request):
    profile = Profile.objects.get_or_create(user=request.user)

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

# Debug Testing page
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

    # for the food log age thing
    age = (date.today() - selected_child.dateOfBirth).days // 365
    if age < 0.5:   mealType = FoodLog.mealTypeBaby
    else:           mealType = FoodLog.mealTypeChild
    food_log_form.fields['mealType'].choices = mealType


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


# PDF generation
@login_required
def pdf_children_all(request):
    response = FileResponse(pdf_file_children_all(request),as_attachment=True,filename='childrenALl.pdf')
    return response

@login_required
def pdf_file_children_all(request):
    children = request.user.children.all()

    from io import BytesIO
    buffer = BytesIO()

    p = canvas.Canvas(buffer)

    page_height = 792
    page_width = 612


    lineHeight = 20;
    leftMargin= 100
    verticalPos = 800

    p.setFont("Courier", lineHeight/1.5)

    verticalPos -= lineHeight * 2

    p.drawString(leftMargin, verticalPos, "Children Info")

    verticalPos -= lineHeight * 2

    def drawLog(logName, logData, leftMargin, verticalPos):
        p.drawString(leftMargin, verticalPos, f"Logs : {logName}")
        verticalPos -= lineHeight
        leftMargin += 20
        logs = logData
        logCount = 0
        for log in logs:
            logCount += 1
            p.drawString(leftMargin, verticalPos, f"Log : {logCount}")
            verticalPos -= lineHeight
        if logCount == 0:
            p.drawString(leftMargin, verticalPos, f"No {logName} Logs")
            verticalPos -= lineHeight
        leftMargin -= 20
        return leftMargin, verticalPos

    for child in children:
        verticalPos -= lineHeight
        p.drawString(leftMargin, verticalPos, f"Name : {child.firstName}, {child.lastName}")
        verticalPos -= lineHeight
        p.drawString(leftMargin, verticalPos, f"DoB  : {child.dateOfBirth}")
        verticalPos -= lineHeight
        p.drawString(leftMargin, verticalPos, f"Code : {child.shareCode}")
        verticalPos -= lineHeight

        leftMargin, verticalPos = drawLog("Growth", child.growthLogs.all(), leftMargin, verticalPos)
        leftMargin, verticalPos = drawLog("Food", child.foodLogs.all(), leftMargin, verticalPos)
        leftMargin, verticalPos = drawLog("Sleep", child.sleepLogs.all(), leftMargin, verticalPos)

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer