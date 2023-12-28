from datetime import date
from rest_framework.permissions import SAFE_METHODS, BasePermission

from users.models import UserSales, UserSupport


class EventPermission(BasePermission):
    """
    Set permissions for access to contracts.

    Sales staff can:
    - create an event
    - view all events in read-only
    Support staff can:
    - update an event assigned to them until the end of the event
    - view all events in read-only
    """

    def has_permission(self, request, view):
        """Set global level permissions for events."""
        current_user = request.user
        if not current_user.is_authenticated:
            return False
        if request.method in SAFE_METHODS and (
                UserSales.objects.filter(user_id=current_user)
                or UserSupport.objects.filter(user_id=current_user)):
            return True
        if request.method in ['POST'] and UserSales.objects.filter(
                user_id=current_user).exists():
            return True
        if request.method in ['PATCH'] and UserSupport.objects.filter(
                user_id=current_user).exists():
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """Set object level permissions for events."""
        current_user = request.user
        if request.method in SAFE_METHODS and (
                UserSales.objects.filter(user_id=current_user) or UserSupport.objects.filter(user_id=current_user)):
            return True
        if request.method == 'POST' \
                and UserSales.objects.filter(user_id=current_user).exists() \
                and request.user.id in obj.users.filter(user_id=current_user.id).values_list('user_id', flat=True):
            return True
        if request.method == 'PATCH' \
                and UserSupport.objects.filter(user_id=current_user).exists() \
                and request.user.id in obj.users.filter(user_id=current_user.id).values_list('user_id', flat=True) \
                and obj.event_date >= date.today():
            return True
        return False
