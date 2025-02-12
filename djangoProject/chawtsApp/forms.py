from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Child, SleepLog, FoodLog, GrowthLog

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# testing out extended user stuff like profile picutre
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']


# for a new child
class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['firstName','lastName','dateOfBirth']

class ShareCodeForm(forms.Form):
    shareCode = forms.CharField(max_length=10)


# tracking Logs
class SleepLogForm(forms.ModelForm):
    class Meta:
        model = SleepLog
        fields = ['timeEvent', 'type', 'duration', 'tag', 'comments']

class FoodLogForm(forms.ModelForm):
    class Meta:
        model = FoodLog
        fields = ['timeEvent', 'type', 'calories', 'tag', 'comments']

class GrowthLogForm(forms.ModelForm):
    class Meta:
        model = GrowthLog
        fields = ['timeEvent', 'height', 'weight', 'headCircumfrance', 'tag', 'comments']