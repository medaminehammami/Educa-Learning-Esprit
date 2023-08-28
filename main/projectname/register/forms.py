from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser 

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField(choices=CustomUser.Role.choices)
    class Meta:
        model = CustomUser  
        fields = ('username', 'email', 'password1', 'password2', 'role')

class UserProfileUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser 
        fields = ('username', 'email')  




