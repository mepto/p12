from django.db import models


class Event(models.Model):
    """Store event information."""
    user = models.ManyToManyField('UserSupport')
    name = models.CharField(max_length=255, blank=True)
    status_event = models.ForeignKey('StatusEvent', on_delete=models.CASCADE, )
    contract = models.ForeignKey('Contract', on_delete=models.CASCADE, )
    attendees = models.IntegerField(blank=True)
    event_date = models.DateField()
    notes = models.TextField(null=False, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-event_date']

    def __str__(self):
        return self.name
