"""Epic Events URL configuration."""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
# from rest_framework_nested.routers import NestedSimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
# router.register('signup', UserViewSet, basename='signup')

epic_header = 'Epic Events administration'
admin.site.site_header = epic_header
admin.site.index_title = epic_header
admin.site.site_title = epic_header

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='token-new'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
