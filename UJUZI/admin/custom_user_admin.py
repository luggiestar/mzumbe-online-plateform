from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin

from ..forms import CustomUserCreationForm, CustomUserChangeForm
from ..models import *
# from .resources import AcademicRegistrationResource

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'first_name','middle_name', 'last_name', 'phone', 'sex', 'is_active', 'is_staff',
                    'is_superuser', 'is_instructor','is_verifier', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'middle_name', 'last_name', 'sex', 'phone')}),

        ('Permissions', {'fields': ('is_superuser','is_staff','is_instructor','is_verifier', 'is_active', 'groups',
                                    'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
