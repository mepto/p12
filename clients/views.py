from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from clients.models import Client
from clients.permissions import ClientPermission
from clients.serializers import ClientSerializer


class ClientViewSet(ModelViewSet):
    """View for clients."""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, ClientPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['last_name', 'first_name', 'email', 'company']
