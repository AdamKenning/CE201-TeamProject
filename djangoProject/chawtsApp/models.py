from django.db import models
from django.contrib.auth.models import User

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
    profile_picture = models.ImageField(upload_to=profilePicUniqueUpload, blank=True, null=True, default='profiles/default.jpg')

    def __str__(self):
        return self.user.username
