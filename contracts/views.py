from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from contracts.models import Contract
from contracts.permissions import ContractPermission
from contracts.serializers import ContractSerializer


class ContractViewSet(ModelViewSet):
    """View for clients."""
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, ContractPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'date_created', 'amount', 'client__company', 'client__email', 'client__last_name']
