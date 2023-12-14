from django.contrib.auth.forms import UserCreationForm, UserChangeForm     # extending these forms into our forms
from .models import CustomUser 

class CustomUserCreationForm(UserCreationForm): #here we are overriding model and fields we are adding to them 
    class Meta(UserCreationForm):
        model = CustomUser 
        fields = UserCreationForm.Meta.fields + ('email', 'role', 'team')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser 
        fields = UserChangeForm.Meta.fields