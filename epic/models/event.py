from django.db import models

from epic.classes import CapitalizeField, UppercaseField


class Event(models.Model):
    """Store event information."""

    status_event = models.ForeignKey('StatusEvent', on_delete=models.CASCADE, )
    contract = models.ForeignKey('Contract', on_delete=models.CASCADE, )
    attendees = models.IntegerField()
    event_date = models.DateField()
    notes = models.TextField(null=False)
    date_created = models.DateTimeField(auto_created=True)
    date_modified = models.DateTimeField(auto_now=True)
