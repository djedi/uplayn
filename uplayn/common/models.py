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

class GameTime(models.Model):
    # follows http://docs.python.org/library/datetime.html#datetime.date.weekday
    WEEKDAY_CHOICES = (
        (6, 'Sunday'),
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
    )
    group = models.ForeignKey(Group)
    weekday = models.IntegerField(choices=WEEKDAY_CHOICES)
    time = models.TimeField()
