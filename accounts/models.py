from django.db import models
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.signals import pre_save
from .utils import slug_pre_save_receiver
# Create your models here.

class Usermanager(BaseUserManager):
    def create_user(self,email,password, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("users must have password")

        email = self.normalize_email(email)
        new_user = self.model(email=email,**extra_fields)
        new_user.set_password(password)
        new_user.save()
        return new_user


    def create_superuser(self, password, email,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser should have is_staff as True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser should have is_super as True')

        if extra_fields.get('is_active') is not True:
            raise ValueError('superuser should have is_active as True')

        return  self.create_user(email,password,**extra_fields)



class User(AbstractUser):
    username = models.CharField(max_length=55)
    email = models.EmailField(max_length=80,unique=True)
    dob = models.DateField(null=True, blank=True)
    Gender = (
        ('MALE', 'male'),
        ('FEMALE', 'female')
    )
    gender = models.CharField(max_length=12, choices=Gender, default='MALE')
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, blank=True, null=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']
    objects = Usermanager()

    def __str__(self):
        return self.username

pre_save.connect(slug_pre_save_receiver,sender=User)




