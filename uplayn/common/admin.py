from django.contrib import admin
from uplayn.common import models

class GroupProfileAdmin(admin.ModelAdmin):
    list_display = ('group', 'subdomain', 'city', 'state', 'zip_code')
admin.site.register(models.GroupProfile, GroupProfileAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'sms_number')
admin.site.register(models.UserProfile, UserProfileAdmin)
