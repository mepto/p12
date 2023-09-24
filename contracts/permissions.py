from rest_framework.permissions import SAFE_METHODS, BasePermission

from users.models import UserSales, UserSupport


class ContractPermission(BasePermission):
    """
    Set permissions for access to contracts.

    Sales staff can:
    - create a contract
    - modify contracts affected to them
    - view all contracts in read-only
    Support can:
    - view all contracts in read-only
    """

    def has_permission(self, request, view):
        """Set global level permissions for contracts."""
        current_user = request.user
        if not current_user.is_authenticated:
            return False
        if request.method in SAFE_METHODS and (
                UserSales.objects.filter(user_id=current_user) or UserSupport.objects.filter(user_id=current_user)):
            return True
        if request.method in ['POST'] and UserSales.objects.filter(
                user_id=current_user).exists():
            return True
        if request.method in ['PATCH', 'DELETE'] and UserSales.objects.filter(
                user_id=current_user).exists():
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """Set object level permissions for contracts."""
        current_user = request.user
        if (request.method in SAFE_METHODS and (
                UserSales.objects.filter(user_id=current_user) or UserSupport.objects.filter(user_id=current_user))):
            return True
        if request.method in ['POST'] and UserSales.objects.filter(user_id=current_user).exists():
            return True
        if request.method in ['PATCH', 'DELETE'] and UserSales.objects.filter(user_id=current_user).exists() \
                and request.user.id in obj.users.filter(user_id=current_user.id).values_list('user_id', flat=True):
            return True
        return False
