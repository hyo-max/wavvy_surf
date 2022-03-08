from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UserChangeForm
from django.forms import EmailField
from .models import User



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')

'''
class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'name')


class LoginForm(AuthenticationForm):
    username = EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))

    '''
class UserUpadateForm(forms.ModelForm):
    email = User.email
    img = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username','img']
