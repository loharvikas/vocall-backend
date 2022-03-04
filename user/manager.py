from django.contrib.auth.base_user import BaseUserManager
from django.forms import ValidationError

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("You must provide an email address.")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned is_superuser=True")

        return self.create_user(email, password, **extra_fields)