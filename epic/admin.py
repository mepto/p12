from django.contrib import admin
from django.contrib.auth.models import Group

from epic.models.client import Client
from epic.models.contract import Contract
from epic.models.event import Event
from epic.models.status import StatusContract, StatusEvent
from epic.models.user import User, UserManagement, UserSales, UserSupport


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


class EventAdmin(admin.ModelAdmin):
    """Display events in admin."""
    # list_display = [f.name for f in self.model._meta.get_fields()]
    fieldsets = [
        ('Event data', {'fields': ['name', 'event_date', 'status_event', 'attendees', 'notes']}),
        ('Event administration', {'fields': ['user', 'contract', 'date_created', 'date_modified']}),
    ]
    filter_horizontal = ('user',)
    readonly_fields = ['date_modified', 'date_created']

    class Meta:
        ordering = ['-event_date']


class ClientAdmin(admin.ModelAdmin):
    """Display clients in admin."""
    fieldsets = [
        ('Client data', {'fields': ['company', 'is_prospect', 'last_name', 'first_name', 'email', 'phone', 'mobile',
                                    'address']}),
        ('Client administration', {'fields': ['user', 'primary_contact', 'date_created', 'date_modified']}),
    ]
    filter_horizontal = ('user',)
    readonly_fields = ['date_modified', 'date_created']

    class Meta:
        ordering = ['company']


class ContractAdmin(admin.ModelAdmin):
    """Display contracts in admin."""
    fieldsets = [
        ('Contract data', {'fields': ['client', 'status_contract', 'amount', 'due_date']}),
        ('Contract administration', {'fields': ['user', 'date_created', 'date_modified']}),
    ]
    filter_horizontal = ('user',)
    readonly_fields = ['date_modified', 'date_created']

    class Meta:
        ordering = ['-due_date']


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(UserSales, UserSalesAdmin)
admin.site.register(UserSupport, UserSupportAdmin)
admin.site.register(UserManagement, UserManagementAdmin)
admin.site.register(StatusEvent)
admin.site.register(StatusContract)
admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)
