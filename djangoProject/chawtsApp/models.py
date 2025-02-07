from django.db import models
from django.contrib.auth.models import User

import random
import string
from django.utils.crypto import get_random_string

import os
from uuid import uuid4

# to disable duplicate profile picture file names
def profilePicUniqueUpload(instance, fileName):
    # Generate a unique filename using UUID
    fileExtension = fileName.split('.')[-1]  # Get file extension
    fileNameUnique = f"{uuid4().hex}.{fileExtension}"

    # Save to 'profiles/' directory
    return os.path.join('profiles/', fileNameUnique)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to=profilePicUniqueUpload,
        blank=True, null=True
    )

    def __str__(self):
        return self.user.username
    class Meta:
        db_table = "chawts_entityParents"
        db_table_comment = "An extension of the django User model for some extra info"

class Child(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dateOfBirth = models.DateField(default=None)

    parents = models.ManyToManyField(User, through='FamilyAssociation', related_name='children')


    # shareCode is whats used for sharing child access between parents
    shareCode = models.CharField(max_length=10, unique=True, blank=True, null=True)
    def shareCodeGenerate(self):
        self.shareCode = get_random_string(length=10)
        self.save()

    class Meta:
        db_table = "chawts_entityChildren"


class FamilyAssociation(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)

    # incase of multiple "parents" e.g. nanny, nurse, father etc
    is_primary = models.BooleanField(default=False)

    class Meta:
        db_table = "chawts_FamilyAssociation"
        unique_together = ('parent', 'child')
        db_table_comment = "Stores who the parents are of which children"



class Log(models.Model):
    TYPES = [
        ('sleep', 'Sleep'),
        ('food', 'Food'),
        ('growth', 'Growth'),
    ]

    type = models.CharField(max_length=50, choices=TYPES)

    timeEntry = models.DateTimeField(auto_now_add=True) # time of when the user logged the event
    timeEvent = models.DateTimeField()                  # time the user claimed the event happend (e.g. logging a meal after the fact)

    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='logs')

    # quick user-defined tags for the user to search by
    tag = models.CharField(max_length=50, blank=True, null=True)

    # more indepth comments if the user wants to say something specific
    comments = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "chawts_log"
        abstract = True

class SleepLog(Log):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='sleep_logs')
    TYPES = [
        ('sleep', 'Sleep'),
        ('nap','Nap'),
        ('siesta','Siesta'),
    ]

    type = models.CharField(max_length=50, choices=TYPES)
    duration = models.DurationField()

    class Meta:
        db_table = "chawts_logSleep"

class FoodLog(Log):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='food_logs')

    TYPES = [
        ('breakfast', 'Breakfast'),
        ('lunch','Lunch'),
        ('dinner','Dinner'),
        ('snack','Snack'),
    ]

    type = models.CharField(max_length=50, choices=TYPES)
    calories = models.IntegerField()

    class Meta:
        db_table = "chawts_logFood"

class GrowthLog(Log):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='growth_logs')

    height = models.FloatField()
    weight = models.FloatField()
    headCircumfrance = models.FloatField()

    class Meta:
        db_table = "chawts_logGrowth"
