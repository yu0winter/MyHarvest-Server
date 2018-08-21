from django.db import models
from django import forms
# Create your models here.
class UserFrom (forms.Form):
    username = forms.CharField()
    password = forms.CharField()


