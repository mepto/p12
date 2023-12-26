from rest_framework import serializers
from rest_framework.fields import DateTimeField

from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    """Serialize Event model."""

    date_created = DateTimeField(required=False, read_only=True)
    date_modified = DateTimeField(required=False, read_only=True)

    class Meta:
        """Meta class."""
        model = Event
        fields = ['id', 'users', 'status_event', 'contract', 'attendees', 'event_date', 'notes',
                  'name', 'date_created', 'date_modified']
