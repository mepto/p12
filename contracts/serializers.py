# recherche sur le nom du client, l'email du client, date du contrat, montant du contrat
# équipe vente peut
# - créer un contrat pour un événement potentiel
# - afficher en RO tous les contrats
# - afficher et modifier les contrats des clients qui leur sont attribués
# équipe support peur
# afficher RO tous les contracts
from rest_framework import serializers
from rest_framework.fields import DateTimeField

from contracts.models import Contract

# from rest_framework.exceptions import ValidationError
# from rest_framework.fields import ChoiceField, DateTimeField
# from rest_framework.relations import PrimaryKeyRelatedField


class ContractSerializer(serializers.ModelSerializer):
    """Serialize Contract model."""

    date_created = DateTimeField(required=False, read_only=True)
    date_modified = DateTimeField(required=False, read_only=True)

    class Meta:
        """Meta class."""
        model = Contract
        fields = ['id', 'user', 'status_contract', 'client', 'amount', 'due_date', 'date_created', 'date_modified']
