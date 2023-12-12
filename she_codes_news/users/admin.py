from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth import get_user_model

from .models import CustomUser
# from .forms import CustomUserCreationForm, CustomUserChangeForm

admin.site.register(CustomUser)
