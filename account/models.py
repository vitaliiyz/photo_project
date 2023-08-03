from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=User)
def hash_passwd(sender, instance, **kwargs):
    if (instance.id is None) or (sender.objects.get(id=instance.id).password != instance.password):
        instance.set_password(instance.password)
