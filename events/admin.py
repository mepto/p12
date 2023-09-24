from django.contrib import admin
from rules.contrib.admin import ObjectPermissionsModelAdmin

from events.models import Event


class EventAdmin(ObjectPermissionsModelAdmin):
    """Display events in admin."""
    list_display = ('name', 'status_event', 'event_date',)
    fieldsets = [
        ('Event data', {'fields': ['name', 'event_date', 'status_event', 'attendees', 'notes']}),
        ('Event administration', {'fields': ['users', 'contract', 'date_created', 'date_modified']}),
    ]
    filter_horizontal = ('users',)
    readonly_fields = ['date_modified', 'date_created']
    search_fields = ['contract__client__last_name', 'contract__client__first_name',
                     'contract__client__email', 'contract__client__company',
                     'event_date']

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('name', 'status_event', 'event_date', 'contract', 'attendees', 'notes', 'users'),
            },
        ),
    )

    class Meta:
        """Meta class."""
        ordering = ['-event_date']


admin.site.register(Event, EventAdmin)
