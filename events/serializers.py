# recherche sur le nom du client, l'email du client, date événement
# équipe de vente peut
# - créer des événements pour un contrat
# - afficher en RO tous les événements
# équipe de support peut
# - afficher et mettre à jour les événements qui leur sont attribués
# jusqu'à la fin de l'événement
# - afficher en RO tous les events
from rest_framework import serializers
from rest_framework.fields import DateTimeField

from events.models import Event

# from rest_framework.exceptions import ValidationError
# from rest_framework.fields import ChoiceField, DateTimeField
# from rest_framework.relations import PrimaryKeyRelatedField


class EventSerializer(serializers.ModelSerializer):
    """Serialize Event model."""

    date_created = DateTimeField(required=False, read_only=True)
    date_modified = DateTimeField(required=False, read_only=True)

    class Meta:
        """Meta class."""
        model = Event
        fields = ['id', 'user', 'status_contract', 'contract', 'attendees', 'event_date', 'notes', 'date_created',
                  'date_modified']
