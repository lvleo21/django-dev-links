from django.db.models import signals
from django.dispatch import receiver
from django.db import transaction

from .models import Account, Profile


@receiver(signals.post_save, sender=Account)
def account_post_save(sender, instance, created, **kwargs):
    if created:
        try:
            with transaction.atomic():
                Profile.objects.create(
                    account=instance
                )
        except Exception as e:
            print(e)
