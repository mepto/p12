from django.contrib import admin

from epic.models import StatusEvent
from events.models import Event


class EventAdmin(admin.ModelAdmin):
    """Display events in admin."""
    # list_display = [f.name for f in self.model._meta.get_fields()]
    fieldsets = [
        ('Event data', {'fields': ['name', 'event_date', 'status_event', 'attendees', 'notes']}),
        ('Event administration', {'fields': ['users', 'contract', 'date_created', 'date_modified']}),
    ]
    filter_horizontal = ('users',)
    readonly_fields = ['date_modified', 'date_created']

    class Meta:
        """Meta class."""
        ordering = ['-event_date']


admin.site.register(StatusEvent)
admin.site.register(Event, EventAdmin)
