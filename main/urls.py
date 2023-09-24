"""Epic Events URL configuration."""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from clients.views import ClientViewSet
from contracts.views import ContractViewSet
from events.views import EventViewSet

client_router = DefaultRouter()
client_router.register('clients', ClientViewSet, basename='clients')
event_router = DefaultRouter()
event_router.register('events', EventViewSet, basename='events')
contract_router = DefaultRouter()
contract_router.register('contracts', ContractViewSet, basename='contracts')

epic_header = 'Epic Events administration'
admin.site.site_header = epic_header
admin.site.index_title = epic_header
admin.site.site_title = epic_header

urlpatterns = [
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(), name='admin_password_reset'),
    path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('admin/', admin.site.urls),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('api/login/', TokenObtainPairView.as_view(), name='token-new'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('api/', include(client_router.urls)),
    path('api/', include(contract_router.urls)),
    path('api/', include(event_router.urls)),
]
