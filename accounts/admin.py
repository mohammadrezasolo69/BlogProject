from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User
from accounts.forms import CustomUserChangeForm, CustomUserCreationForm


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ['username', 'email', 'is_author', 'is_staff', 'is_active']
    list_editable = ('is_author', 'is_active')
    list_filter = ('is_author', 'is_active')

    fieldsets = UserAdmin.fieldsets + (
        ('author', {'fields': ('is_author',)}),
    )
