from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

import os
from uuid import uuid4

# to disable duplicate profile picture file names (profile & child)
def profilePicUniqueUpload(instance, fileName):
    # Generate a unique filename using UUID
    fileExtension = fileName.split('.')[-1]  # Get file extension
    fileNameUnique = f"{uuid4().hex}.{fileExtension}"

    # Save to 'pfp/' directory
    return os.path.join('pfp/', fileNameUnique)

# An extension of the django User model for some extra info
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to=profilePicUniqueUpload,blank=True, null=True)

    def __str__(self):
        return self.user.username
    class Meta:
        db_table = "chawts_userExtended"

class Child(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dateOfBirth = models.DateField(default=None)

    profile_picture = models.ImageField(upload_to=profilePicUniqueUpload,blank=True, null=True)

    parents = models.ManyToManyField(User, through='FamilyAssociation', related_name='children')


    # shareCode is whats used for sharing child access between parents
    shareCode = models.CharField(max_length=10, unique=True, blank=True, null=True)
    def shareCodeGenerate(self):
        self.shareCode = get_random_string(length=10)
        self.save()

    class Meta:
        db_table = "chawts_child"

# Stores who the parents are of which children
class FamilyAssociation(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    ## relationship status : father nanny etc

    # iscase of multiple "parents" e.g. nanny, nurse, father etc
    is_primary = models.BooleanField(default=False)

    class Meta:
        db_table = "chawts_families"
        unique_together = ('parent', 'child')

class Log(models.Model):
    TYPES = [
        ('sleep', 'Sleep'),
        ('food', 'Food'),
        ('growth', 'Growth'),
    ]

    type = models.CharField(max_length=50, choices=TYPES)

    timeEntry = models.DateTimeField(auto_now_add=True)     # time of when the user logged the event
    timeEvent = models.DateTimeField(default=timezone.now)  # time the user claimed the event happened (e.g. logging a meal after the fact)

    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='logs')

    # quick comments to label the log
    comment = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = "chawts_logBasic"
        abstract = True

class SleepLog(Log):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='sleepLogs')
    TYPES = [
        ('sleep', 'Sleep'),
        ('nap','Nap'),
        ('siesta','Siesta'),
    ]

    type = models.CharField(max_length=50, choices=TYPES)
    duration = models.DurationField()

    class Meta:
        db_table = "chawts_logSleep"

# adjusted to match project description
class FoodLog(Log):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='foodLogs')

    # Meal options if child age < 6 months
    mealTypeBaby = [
        ('formula','Formula'),
        ('cowMilk','Cow Milk'),
        ('breastMilk','Breast Milk'),
    ]

    # Meal options if child age > 6 months
    mealTypeChild = [
        ('pasta', 'Pasta'),
        ('jacketPotato','Jacket potato'),
        ('chickenCurryWithRice','Chicken curry with rice'),
        ('risotto','Risotto'),
        ('chilliConCarne','Chilli con carne'),
    ]

    amountEaten = [
        (0.00,'None'),
        (0.25,'Some'),
        (0.50,'Half'),
        (0.75,'Most'),
        (1.00,'Full'),
    ]

    mealType = models.CharField(max_length=50, choices=[])
    amount = models.DecimalField(max_digits=3,decimal_places=2, choices=amountEaten,default=1.00)
    calories = models.IntegerField()

    class Meta:
        db_table = "chawts_logFood"

class GrowthLog(Log):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='growthLogs')

    height = models.FloatField()
    weight = models.FloatField()
    headCircumfrance = models.FloatField()

    class Meta:
        db_table = "chawts_logGrowth"


# class MedicationLog(Log):
#     child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='medicationLogs')

#     class Meta:
#         db_table = "chawts_logMedication"

# class DiaperLog(Log):
#     child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='diaperLogs')

#     TYPES = [
#         ('pee', 'Pee'),
#         ('poo', 'Poo'),
#     ]

#     type = models.CharField(max_length=50, choices=TYPES)

#     class Meta:
#         db_table = "chawts_logDiaper"

# class EmotionLog(Log):
#     child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='EmotionLogs')

#     class Meta:
#         db_table = "chawts_logEmotion"