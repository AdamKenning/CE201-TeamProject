from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage

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

# class Child(models.Model):
#     name = models.CharField(max_length=255)
#     date_of_birth = models.DateField()
#     parents = models.ManyToManyField(User, related_name="children")  # many to many

#     def __str__(self):
#         return self.name
