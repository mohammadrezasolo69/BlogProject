from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('is_author',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={'class': "input100", 'placeholder': "Enter username"}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': "input100", 'placeholder': "Enter username"}))


class RegisterUserForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': "input100", 'placeholder': "Enter username"})
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': "input100", 'placeholder': "Enter Email"})
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': "input100", 'placeholder': "Enter password"})
    )

    password2 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': "input100", 'placeholder': "Enter confirm password"})
    )

    def clean_password2(self):
        password = self.cleaned_data["password"]
        password2 = self.cleaned_data["password2"]

        if (password and password2) and (password != password2):
            raise forms.ValidationError("The passwords you have entered do not match.")

        return password2

    def clean_email(self):
        email = self.cleaned_data["email"]
        user = get_user_model()
        if user.objects.filter(email=email).exists():
            raise forms.ValidationError('This email already exists')
        return email

    def clean_username(self):
        username = self.cleaned_data["username"]
        user = get_user_model()
        if user.objects.filter(username=username).exists():
            raise forms.ValidationError('This username already exists')
        return username
