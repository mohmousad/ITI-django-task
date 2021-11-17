from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver
from .models import Movie


@receiver(post_delete, sender=Movie)
def notify_admins(**kwargs):
    instance = kwargs.get('instance')
    print("The deleted movie is {}".format(instance))

