# from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from clients.models import Client
from clients.serializers import ClientSerializer


class ClientViewSet(ModelViewSet):
    """View for clients."""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    # def retrieve(self, request, pk=None, *args, **kwargs):
    #     client = get_object_or_404(Client, pk=pk)
    #     print(client)
    #     self.check_object_permissions(self.request, client)
    #     serializer = ClientSerializer(client)
    #     return Response(serializer.data)
    #
    # def update(self, request, pk=None, *args, **kwargs):
    #     client = get_object_or_404(Client, pk=pk)
    #     self.check_object_permissions(self.request, client)
    #     serializer = ClientSerializer(client, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def destroy(self, request, pk=None):
    #     client = get_object_or_404(Client, pk=pk)
    #     self.check_object_permissions(self.request, client)
    #     client.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
