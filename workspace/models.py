from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Workspace(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workspaces")
    create_date = models.DateField(default= timezone.now)
    last_modified_date = models.DateField(default= timezone.now)

    def __str__(self):
        return f'{self.name} | {self.user.email}'

    def save(self, *args, **kwargs):
        self.last_modified_date = timezone.now()
        super(Workspace, self).save(*args, **kwargs)

    