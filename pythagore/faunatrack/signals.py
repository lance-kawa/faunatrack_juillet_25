from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from faunatrack.models import FaunatrackUser

@receiver(post_save, sender=User)
def create_faunatrack_user(sender, instance, created, **kwargs):
    if created:
        FaunatrackUser.objects.create(user=instance)

