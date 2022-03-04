from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from user.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("Email Address", unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)

    date_joined = models.DateTimeField(default=timezone.now)
    last_modified_date = models.DateTimeField(default=timezone.now)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELD = []

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.last_modified_date = timezone.now()
        super(User, self).save(*args, **kwargs)
