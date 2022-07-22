import email
from django import forms
from django.forms import ModelForm
from main.models import UserProfile
from django.contrib.auth.models import User


class UserForm(ModelForm):
    first_name = forms.CharField(label='First Name', max_length=10)
    last_name = forms.CharField(label='Last Name', max_length=10)
    email = forms.EmailField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class UserProfileForm(ModelForm):
    class Meta():
        model = UserProfile
        exclude = ['user']


# trying something irrelevant here.....
class ContactForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message')
    sender = forms.EmailField(label='Sender')
    cc_myself = forms.BooleanField(required=False)