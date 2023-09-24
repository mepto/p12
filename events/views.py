from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from events.models import Event
from events.permissions import EventPermission
from events.serializers import EventSerializer


class EventViewSet(ModelViewSet):
    """View for clients."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, EventPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['contract__client__last_name', 'contract__client__first_name',
                     'contract__client__email', 'contract__client__company',
                     'event_date']
