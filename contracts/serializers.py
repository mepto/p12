from rest_framework import serializers
from rest_framework.fields import DateTimeField

from contracts.models import Contract


class ContractSerializer(serializers.ModelSerializer):
    """Serialize Contract model."""

    date_created = DateTimeField(required=False, read_only=True)
    date_modified = DateTimeField(required=False, read_only=True)

    class Meta:
        """Meta class."""
        model = Contract
        fields = ['id', 'users', 'status_contract', 'client', 'amount', 'due_date', 'date_created', 'date_modified']
