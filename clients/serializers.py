from rest_framework import serializers
from rest_framework.fields import DateTimeField

from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    """Serialize Client model."""

    date_created = DateTimeField(required=False, read_only=True)
    date_modified = DateTimeField(required=False, read_only=True)

    class Meta:
        """Meta class."""
        model = Client
        fields = ['id', 'users', 'company', 'first_name', 'last_name', 'email', 'phone', 'mobile', 'address',
                  'is_prospect', 'primary_contact', 'date_created', 'date_modified']
