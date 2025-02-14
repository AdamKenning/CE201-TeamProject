from django.db.models.signals import pre_save, pre_delete
from django.db.models.signals import post_save
from django.core.files.storage import default_storage
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

# profile setup
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created and not Profile.objects.filter(user=instance).exists():
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


# cleaning up unused profile pictures
@receiver(pre_save, sender=Profile)
def delete_old_file_on_update(sender, instance, **kwargs):
    if not instance.pk:
        # if new object, nothing to delete
        return

    try:
        old_instance = Profile.objects.get(pk=instance.pk)
        if old_instance.profile_picture and old_instance.profile_picture != instance.profile_picture:
            # delete old image if image being replaced
            if default_storage.exists(old_instance.profile_picture.path):
                default_storage.delete(old_instance.profile_picture.path)
    except Profile.DoesNotExist:
        # if new object, nothing to delete
        pass

# delete profile picture on profile deletion (...user deletion)
@receiver(pre_delete, sender=Profile)
def delete_file_on_profile_delete(sender, instance, **kwargs):
    if instance.profile_picture:
        # delete associated file
        if default_storage.exists(instance.profile_picture.path):
            default_storage.delete(instance.profile_picture.path)
