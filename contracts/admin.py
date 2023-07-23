from django.contrib import admin

from contracts.models import Contract
from epic.models import StatusContract


class ContractAdmin(admin.ModelAdmin):
    """Display contracts in admin."""
    fieldsets = [
        ('Contract data', {'fields': ['client', 'status_contract', 'amount', 'due_date']}),
        ('Contract administration', {'fields': ['users', 'date_created', 'date_modified']}),
    ]
    filter_horizontal = ('users',)
    readonly_fields = ['date_modified', 'date_created']

    class Meta:
        """Meta class."""
        ordering = ['-due_date']


admin.site.register(StatusContract)
admin.site.register(Contract, ContractAdmin)
