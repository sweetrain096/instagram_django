from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCustomCreationFrom(UserCreationForm):
    class Meta:
        model = get_user_model()
        # fields = '__all__'
        fields = ['username', 'email', 'password1', 'password2']