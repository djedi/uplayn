from django.db import models
from django.contrib.auth.models import User, Group

class GroupProfile(models.Model):
    group = models.OneToOneField(Group)
    subdomain = models.SlugField(unique=True)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=10)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    sms_number = models.CharField(max_length=32)
