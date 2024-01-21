from django.db.models.signals import post_save
from django.dispatch import receiver
from loguru import logger
from rest_framework.authentication import get_user_model

from .models import UserProfile


@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created, **kwargs):
    if created:
        logger.debug("Created profile for {}", instance)
        UserProfile.objects.create(user=instance)
