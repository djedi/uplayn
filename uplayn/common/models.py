from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    subdomain = models.SlugField()
    
    
class Profile(models.Model):
    user = models.OneToOneField(User)
    groups = models.ManyToManyField(Group)

