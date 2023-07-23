from django.contrib import admin

from users.models import User, UserManagement, UserSales, UserSupport


class UserAdmin(admin.ModelAdmin):
    """Set admin for base user."""
    fieldsets = [
        ('User profile', {'fields': ['email', 'last_name', 'first_name']}),
    ]
    list_display = (
        'email', 'last_name', 'first_name', 'is_active', 'is_superuser', 'is_staff', 'date_joined', 'date_modified')
    search_fields = ['email', 'last_name', 'first_name']
    list_filter = ['is_active']


class UserManagementAdmin(admin.ModelAdmin):
    """Display management user admin."""
    list_display = ('user',)
    search_fields = ['user__last_name', 'user__first_name', 'user__email', 'user__is_active']


class UserSupportAdmin(admin.ModelAdmin):
    """Display management user admin."""
    list_display = ('user',)
    search_fields = ['user__last_name', 'user__first_name', 'user__email', 'user__is_active']


class UserSalesAdmin(admin.ModelAdmin):
    """Display management user admin."""
    list_display = ('user',)
    search_fields = ['user__last_name', 'user__first_name', 'user__email', 'user__is_active']


admin.site.register(User, UserAdmin)
admin.site.register(UserSales, UserSalesAdmin)
admin.site.register(UserSupport, UserSupportAdmin)
admin.site.register(UserManagement, UserManagementAdmin)
