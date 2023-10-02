from django.db import models


class Contract(models.Model):
    """Store contracts information."""

    users = models.ManyToManyField('users.UserSales', related_name='contracts')
    status_contract = models.ForeignKey('epic.StatusContract', on_delete=models.CASCADE, related_name='contracts')
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE, related_name='contracts')
    amount = models.IntegerField(blank=True, help_text='Amounts should always be entered in cents')
    due_date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class."""
        ordering = ['-due_date']

    def __str__(self):
        """Default human-readable return for contract object."""
        return f'Contract No. {self.id} ({self.client})'

    @property
    def amount_in_euros(self):
        return f'{str(self.amount)[:(len(str(self.amount))-2)]}.{str(self.amount)[-2:]} €'
