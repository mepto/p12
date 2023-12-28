from rest_framework import serializers
from rest_framework.fields import DateTimeField

from clients.models import Client
from contracts.models import Contract


class ContractSerializer(serializers.ModelSerializer):
    """Serialize Contract model."""

    date_created = DateTimeField(required=False, read_only=True)
    date_modified = DateTimeField(required=False, read_only=True)

    class Meta:
        """Meta class."""
        model = Contract
        fields = ['id', 'users', 'status_contract', 'client', 'amount', 'due_date', 'date_created', 'date_modified']

    def create(self, validated_data):
        """Change client prospect status on contract creation."""
        instance = super().create(validated_data)
        current_client = Client.objects.get(id=validated_data['client'].id)
        current_client.is_prospect = False
        current_client.save()
        return instance
