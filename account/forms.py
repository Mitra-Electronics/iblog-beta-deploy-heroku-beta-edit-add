from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile

# sign up form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'first name', 'class': 'form-control'})
    )
    last_name = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'last name', 'class': 'form-control'})
    )
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
        fields = ('username', 'first_name' ,'email', 'password1', 'password2')

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
    about = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'About', 'class': 'form-control'})
    )
    website = forms.URLField(
        required=True,
        label="",
        widget=forms.URLInput(attrs={'placeholder': 'URL', 'class': 'form-control'})
    )
    profile_picture = forms.ImageField(
        required=True,
        label="",
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Profile
        exclude = ['user', 'fullname']
