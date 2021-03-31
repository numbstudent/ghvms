from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label='Nama Lengkap',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Nama Lengkap'})
    )
    username = forms.CharField(
        label='User ID',
        max_length=100, widget=forms.TextInput(attrs={'placeholder': 'User ID'})
    )
    email = forms.EmailField(label='Email', max_length=100)
    password1 = forms.CharField(
        label='Password', max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Ulangi Password', max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2' )


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='User ID',
        max_length=100, widget=forms.TextInput(attrs={'placeholder': 'User ID'})
    )
    password = forms.CharField(
        label='Password', max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','password')
