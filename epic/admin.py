from django.contrib import admin
from django.contrib.auth.models import Group

from epic.models.client import Client
from epic.models.contract import Contract
from epic.models.event import Event
from epic.models.status import StatusContract, StatusEvent
from epic.models.user import User, UserManagement, UserSales, UserSupport


class UserAdmin(admin.ModelAdmin):
    """"""
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


admin.site.unregister(Group)
# admin.site.register(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserSales, UserSalesAdmin)
admin.site.register(UserSupport, UserSupportAdmin)
admin.site.register(UserManagement, UserManagementAdmin)
admin.site.register(StatusEvent)
admin.site.register(StatusContract)
admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Event)
