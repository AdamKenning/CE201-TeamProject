from django import forms
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']

class ChildEditForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['firstName', 'lastName', 'dateOfBirth', 'profile_picture']
        widgets = {
            'dateOfBirth': forms.DateInput(attrs={'type': 'date'})
        }


# for a new child
class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['firstName','lastName','dateOfBirth','profile_picture']
        widgets = {
            'dateOfBirth': forms.DateInput(attrs={'type': 'date'})
        }

class ShareCodeForm(forms.Form):
    shareCode = forms.CharField(max_length=10)
    shareCode = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'Enter 10 digit share code', 'class': 'code-input'})
    )


# tracking Logs
class SleepLogForm(forms.ModelForm):
    class Meta:
        model = SleepLog
        fields = ['timeEvent', 'type', 'duration', 'comment']
        widgets = {
            'timeEvent': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Add any additional notes ...', 'rows': 3}),
        }

class FoodLogForm(forms.ModelForm):
    # meal_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = FoodLog
        fields = ['timeEvent', 'mealType', 'amount', 'calories', 'comment']
        widgets = {
            'timeEvent': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Add any additional notes ...', 'rows': 3}),
        }

class GrowthLogForm(forms.ModelForm):
    class Meta:
        model = GrowthLog
        fields = ['timeEvent', 'height', 'weight', 'headCircumfrance', 'comment']
        widgets = {
            'timeEvent': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'height': forms.NumberInput(attrs={'placeholder': 'Height (cm)'}),
            'weight': forms.NumberInput(attrs={'placeholder': 'Weight (kg)'}),
            'headCircumfrance': forms.NumberInput(attrs={'placeholder': 'Head Circumference (cm)'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Any extra details?', 'rows': 3}),
        }