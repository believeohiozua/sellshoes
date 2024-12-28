from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances will come from UserAdmin
    model = CustomUser

    # Fields to be displayed in the admin interface
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'is_superuser')

    # Fields to be used in the admin user edit page
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )

    # Fields to be used in the admin user creation form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser'),
        }),
    )
    
    filter_horizontal = ()

    # Fields for search functionality
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

# Register the custom user and admin
admin.site.register(CustomUser, CustomUserAdmin)

