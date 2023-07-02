from django.db import models


class Contract(models.Model):
    """Store contracts information."""

    user = models.ManyToManyField('UserSales')
    status_contract = models.ForeignKey('StatusContract', on_delete=models.CASCADE,)
    client = models.ForeignKey('Client', on_delete=models.CASCADE,)
    amount = models.IntegerField(blank=True)
    due_date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-due_date']

    def __str__(self):
        return f'Contract No. {self.id} ({self.client})'
