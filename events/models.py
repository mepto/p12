from django.db import models


class Event(models.Model):
    """Store event information."""
    users = models.ManyToManyField('users.UserSupport', related_name='events')
    name = models.CharField(max_length=255, blank=True)
    status_event = models.ForeignKey('epic.StatusEvent', on_delete=models.CASCADE, related_name='events')
    contract = models.ForeignKey('contracts.Contract', on_delete=models.CASCADE, related_name='events')
    attendees = models.IntegerField(blank=True)
    event_date = models.DateField()
    notes = models.TextField(null=False, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class."""
        ordering = ['-event_date']

    def __str__(self):
        """Default human-readable return for event object."""
        return self.name
