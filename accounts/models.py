from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from datetime import datetime
from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'{self.name} : {self.email}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Otpcode(models.Model):
    code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=11)
    created_at = models.DateTimeField()
    expires_at = models.DateTimeField()

    def __str__(self):
        return self.code

    @property
    def is_expired(self):
        return self.expires_at < timezone.now()

    def save(self, *args, **kwargs):
        # Set the expiration time to 2 minutes from the current time
        if not self.pk:
            self.expires_at = timezone.now() + timezone.timedelta(minutes=2)
            self.created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        super().save(*args, **kwargs)
