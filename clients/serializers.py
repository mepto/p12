# recherche sur le nom du client, l'email du client
# équipe vente peut
# créer des clients
# afficher et mettre à jour els clients qui leur sont attribués
# afficher en RO tous les clients
# équipe de support
# accès RO à tous les clients
# # peut afficher les clients pour les clients des événements qui leur sont attribués
from rest_framework import serializers
from rest_framework.fields import DateTimeField

from clients.models import Client

# from rest_framework.exceptions import ValidationError
# from rest_framework.fields import ChoiceField, DateTimeField
# from rest_framework.relations import PrimaryKeyRelatedField


class ClientSerializer(serializers.ModelSerializer):
    """Serialize Client model."""

    date_created = DateTimeField(required=False, read_only=True)
    date_modified = DateTimeField(required=False, read_only=True)

    class Meta:
        """Meta class."""
        model = Client
        fields = ['id', 'users', 'company', 'first_name', 'last_name', 'email', 'phone', 'mobile', 'address',
                  'is_prospect', 'primary_contact', 'date_created', 'date_modified']
