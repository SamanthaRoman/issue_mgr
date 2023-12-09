from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import CustomUser 
from .forms import CustomUserCreationForm , CustomUserChangeForm 


# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = UserAdmin.fieldsets + (  # fieldsets shows up on the change form
        # tople with a value fields that also has a tople.
        ("None", {'fields': ('role', 'team')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (   # add_fieldsets shows up on the create user form
        ("None", {'fields': ('email', 'role', 'team')}),
    )
    list_display = [
        "username",
        "email",
        "last_name",
        "first_name",
        "role",
        "team",
        "is_staff",
    ]

admin.site.register(CustomUser, CustomUserAdmin)