from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=128)
    subdomain = models.SlugField()

class Profile(models.Model):
    user = models.OneToOneField(User)
    groups = models.ManyToManyField(Group)
