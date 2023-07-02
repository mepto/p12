from django.db import models

from epic.classes import CapitalizeField, UppercaseField


class Client(models.Model):
    """Store client information."""

    user = models.ManyToManyField('UserSales')
    company = CapitalizeField(max_length=255, null=False)
    first_name = CapitalizeField(max_length=25, blank=True)
    last_name = UppercaseField(max_length=25, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    address = models.TextField(null=False)
    is_prospect = models.BooleanField(default=True)
    primary_contact = models.ForeignKey('User', null=False, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['company']

    def __str__(self):
        return self.company
