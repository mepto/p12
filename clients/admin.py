from django.contrib import admin
from rules.contrib.admin import ObjectPermissionsModelAdmin

from clients.models import Client


class ClientAdmin(ObjectPermissionsModelAdmin):
    """Display clients in admin."""
    fieldsets = [
        ('Client data', {'fields': ['company', 'is_prospect', 'last_name', 'first_name', 'email', 'phone', 'mobile',
                                    'address']}),
        ('Client administration', {'fields': ['users', 'primary_contact', 'date_created', 'date_modified']}),
    ]
    filter_horizontal = ('users',)
    readonly_fields = ['date_modified', 'date_created']
    search_fields = ['last_name', 'first_name', 'email', 'company']

    class Meta:
        """Meta class."""
        ordering = ['company']


admin.site.register(Client, ClientAdmin)
