import re

from django import forms
from django.contrib.auth.models import User, Group

from uplayn.common import models

class StartGroupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    cpassword = forms.CharField(widget=forms.PasswordInput,
        label="Password (again)")
    group_name = forms.CharField()
    subdomain = forms.SlugField(help_text=".uplayn.com")

    def clean(self):
        if 'password' in self.cleaned_data and \
            'cpassword' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['cpassword']:
                raise forms.ValidationError("Your passwords did not match.")
        return self.cleaned_data

    def clean_username(self):
        data = self.cleaned_data['username']
        try:
            username = User.objects.get(username__iexact=data)
        except User.DoesNotExist:
            return data
        raise forms.ValidationError('This username is already taken. Please choose another.')

    def clean_subdomain(self):
        """
        Check to make sure subdomain is unique
        Also, don't allow certain subdomains like 'www'
        """
        subdomain = self.cleaned_data['subdomain']
        exists = models.GroupProfile.objects.filter(
            subdomain__iexact=subdomain).count() == 1
        if exists:
            raise forms.ValidationError("This subdomain is already taken. Please choose another.")

        reserved = ('www', 'admin', 'forum', 'blog', 'ultimate', 'basketball')
        if subdomain in reserved:
            raise forms.ValidationError("This subdomain is reserved. Please choose another.")

        if not re.search('^[a-z\-0-9]*$', subdomain):
            raise forms.ValidationError("This subdomain is invalid. Please enter lowercase letters, numbers and dashes only.")

        if not re.search('^[a-z0-9]', subdomain):
            raise forms.ValidationError("Your subdomain must begin with a lowercase letter or number.")

        return subdomain

    def save(self):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password'],
        )
        user.is_staff = True
        user.save()

        group = models.Group.objects.create(
            name = self.cleaned_data['group_name'])

        user.groups.add(group)

        uprofile = models.UserProfile.objects.create(
            user = user
        )
        gprofile = models.GroupProfile.objects.create(
            group = group,
            subdomain = self.cleaned_data['subdomain'],
        )
