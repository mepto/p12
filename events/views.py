from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from events.models import Event
from events.serializers import EventSerializer


class EventViewSet(ModelViewSet):
    """View for clients."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
