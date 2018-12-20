from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Profile


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(max_length=60, label='First Name')
    last_name = forms.CharField(max_length=60, label='Last Name')
    location = forms.CharField(max_length=30, label='Location')
    phone_number = forms.IntegerField(label='Phone Number')

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2", "location", "phone_number")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user