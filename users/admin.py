from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from rules.contrib.admin import ObjectPermissionsModelAdmin, ObjectPermissionsModelAdminMixin

from users.models import User, UserManagement, UserSales, UserSupport


class UserAdmin(ObjectPermissionsModelAdminMixin, auth_admin.UserAdmin):
    """Set admin for base user."""
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                ),
            },
        ),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2'),
            },
        ),
    )
    list_display = (
        'email', 'username', 'last_name', 'first_name', 'is_active', 'is_superuser', 'is_staff', 'date_joined',
        'date_modified')
    readonly_fields = ['date_joined', 'last_login']
    search_fields = ['email', 'last_name', 'first_name']
    list_filter = ['is_active']
    ordering = ('email',)


class UserManagementAdmin(ObjectPermissionsModelAdmin):
    """Display management user admin."""
    list_display = ('user', )
    search_fields = ['user__last_name', 'user__first_name', 'user__username', 'user__email', 'user__is_active']


class UserSupportAdmin(ObjectPermissionsModelAdmin):
    """Display management user admin."""
    list_display = ('user',)
    search_fields = ['user__last_name', 'user__first_name', 'user__username', 'user__email', 'user__is_active']


class UserSalesAdmin(ObjectPermissionsModelAdmin):
    """Display management user admin."""
    list_display = ('user',)
    search_fields = ['user__last_name', 'user__first_name', 'user__username', 'user__email', 'user__is_active']


admin.site.register(User, UserAdmin)
admin.site.register(UserSales, UserSalesAdmin)
admin.site.register(UserSupport, UserSupportAdmin)
admin.site.register(UserManagement, UserManagementAdmin)
