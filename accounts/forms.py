from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Profile
class UserCustomCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        # fields = '__all__'
        fields = ['username', 'email', 'password1', 'password2']

class UserCustomChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['email']
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        # fields = ['nickname', 'introduction', 'image']