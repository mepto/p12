from django.db import models


class Contract(models.Model):
    """Store contracts information."""

    status_contract = models.ForeignKey('StatusContract', on_delete=models.CASCADE,)
    client = models.ForeignKey('Client', on_delete=models.CASCADE,)
    amount = models.IntegerField()
    due_date = models.DateField()
    date_created = models.DateTimeField(auto_created=True)
    date_modified = models.DateTimeField(auto_now=True)
