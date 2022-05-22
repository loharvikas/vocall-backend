from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Voice


# @receiver(post_delete, sender=Voice)
# def delete_file(sender, instance, **kwargs):
#     instance.file.delete()
