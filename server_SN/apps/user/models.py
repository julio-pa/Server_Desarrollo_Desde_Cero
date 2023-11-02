from django.db import models
from django.utils import timezone
# import uuid
# from django.contrib.auth.models import User, UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Signals
# from django.db.models.signals import post_save

# Manager of users


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


# The base user model

class UserAccount(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=70)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

# The profile date of the user


class ProfileUser(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    img_profile = models.ImageField(
        default='media/images/dyqibe0yx4ibmevfpanb', upload_to='images/')
    bio = models.CharField(max_length=70, blank=True, default='no bio yet')
    joined = models.DateTimeField(default=timezone.now)
    following = models.IntegerField(default=0, blank=True)
    followers = models.IntegerField(default=0, blank=True)
