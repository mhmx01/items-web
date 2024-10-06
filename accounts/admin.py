from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "is_superuser",
    )
    readonly_fields = ("is_staff", "is_active", "is_superuser")
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (
            None,
            {
                "fields": ("username", "email", "password1", "password2"),
                "classes": ("wide",),
            },
        ),
    )
