from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import * 
from .forms import *
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form  = CustomUserChangeForm
    list_display = ('email','username')
admin.site.register(CustomUser , CustomUserAdmin)
# Register your models here.
