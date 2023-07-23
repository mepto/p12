"""Epic Events URL configuration."""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
# from rest_framework_nested.routers import NestedSimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from clients.views import ClientViewSet
# router = DefaultRouter()
# router.register('signup', UserViewSet, basename='signup')
from contracts.views import ContractViewSet
from events.views import EventViewSet

client_router = DefaultRouter()
client_router.register('clients', ClientViewSet, basename='clients')
event_router = SimpleRouter()
event_router.register('events', EventViewSet, basename='events')
contract_router = SimpleRouter()
contract_router.register('contracts', ContractViewSet, basename='contracts')

epic_header = 'Epic Events administration'
admin.site.site_header = epic_header
admin.site.index_title = epic_header
admin.site.site_title = epic_header

urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token-new'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('api/', include(client_router.urls)),
    path('api/', include(contract_router.urls)),
    path('api/', include(event_router.urls)),
]
