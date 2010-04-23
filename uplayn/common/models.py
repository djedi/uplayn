from django.db import models
from django.contrib.auth.models import User, Group

class GroupProfile(models.Model):
    group = models.OneToOneField(Group)
    subdomain = models.SlugField(unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    state = models.CharField(max_length=32, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    map_location = models.CharField(max_length=512, blank=True, null=True)

    def address_string(self):
        return "%s, %s, %s %s" % (self.address, self.city, self.state, self.zip_code)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    sms_number = models.CharField(max_length=32, blank=True, null=True)
