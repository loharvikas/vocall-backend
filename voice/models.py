from django.db import models
from django.utils import timezone
import uuid

from workspace.models import Workspace


# Create your models here.

class Voice(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(upload_to="records")
    active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name="voices")

    created_date = models.DateTimeField(default=timezone.now)
    last_modified_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        self.last_modified_date = timezone.now()
        super(Voice, self).save(*args, **kwargs)
    
