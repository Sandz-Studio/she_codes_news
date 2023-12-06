from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'birth_date','username', 'email', 'profile_photo', 'bio']
        widgets = {
            'birth_date': forms.DateInput(
                format='%m/%d/%Y',
                attrs={
                    'class':'form-control',
                    'placeholder':'Select a date',
                    'type':'date'
                }
            )
        }
        # labels = {
        #     'profile_photo': 'Image URL'
        # }


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'birth_date', 'username', 'email', 'profile_photo', 'bio']