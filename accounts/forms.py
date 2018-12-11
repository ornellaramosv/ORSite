from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(max_length=60, label='First Name')
    last_name = forms.CharField(max_length=60, label='Last Name')

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")
        help_texts = {
            "email": "Hello"
        }

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
