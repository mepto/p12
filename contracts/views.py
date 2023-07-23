from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from contracts.models import Contract
from contracts.serializers import ContractSerializer


class ContractViewSet(ModelViewSet):
    """View for clients."""
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]
