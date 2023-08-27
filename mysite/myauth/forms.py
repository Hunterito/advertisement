from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AdvertisementRegister(UserCreationForm):
    main_attrs = {'class': 'form-control-lg'}

    name = forms.CharField(label="name", widget=forms.TextInput(attrs=main_attrs))
    surname = forms.CharField(label="surname", widget=forms.TextInput(attrs=main_attrs))
    username = forms.CharField(label='username', min_length=5, max_length=150, widget=forms.TextInput(attrs=main_attrs))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(main_attrs))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(main_attrs))

    def save(self, commit=False):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1'],
            first_name=self.cleaned_data['name'],
            last_name=self.cleaned_data['surname']
        )
        return user
