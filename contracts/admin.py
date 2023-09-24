from django.contrib import admin
from rules.contrib.admin import ObjectPermissionsModelAdmin

from contracts.models import Contract


class ContractAdmin(ObjectPermissionsModelAdmin):
    """
    Display contracts in admin.

    Search on contract, client name, client email
    """
    fieldsets = [
        ('Contract data', {'fields': ['client', 'status_contract', 'amount', 'due_date']}),
        ('Contract administration', {'fields': ['users', 'date_created', 'date_modified']}),
    ]
    filter_horizontal = ('users',)
    readonly_fields = ['date_modified', 'date_created']
    search_fields = ['id', 'date_created', 'amount', 'client__company', 'client__email', 'client__last_name']

    class Meta:
        """Meta class."""
        ordering = ['-due_date']


# admin.site.register(StatusContract)
admin.site.register(Contract, ContractAdmin)
