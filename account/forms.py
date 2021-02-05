from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

# sign up form
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'username', 'class':'form-control'})
    )
    email = forms.EmailField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'user@domain.com', 'class':'form-control'}),
        #unique = True
    )
    password1 = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'password', 'class':'form-control'})
    )
    password2 = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 're-enter the password', 'class':'form-control'})
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class' : 'form-control'})
    )
    password = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class' : 'form-control'})
    )
    class Meta:
        model = User
        fields = ['Username', 'Password']

# edit profile form
class EditProfile(forms.ModelForm):
    fullname = forms.CharField(
        required=False,
        label="Full name",
    )
    class Meta:
        model = Profile
        exclude = ['user']
