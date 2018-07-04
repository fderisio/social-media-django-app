from django.db import models
from django import forms


class User(models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=100,
        unique=True,
        help_text='Required.',
    )
    email = models.EmailField(
        max_length=100,
        unique=True,
        help_text='Required.',
    )
    password = models.CharField(
        max_length=50
    )


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'email']
