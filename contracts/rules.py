from rules.permissions import add_perm
from rules.predicates import is_authenticated, predicate

from users.models import UserSales, UserSupport


@predicate
def is_sales(user, obj):
    """Check if user is in sales."""
    return UserSales.objects.filter(user_id=user.id).exists()


@predicate
def is_support(user, obj):
    """Check if user is in support."""
    return UserSupport.objects.filter(user_id=user.id).exists()


@predicate
def is_listed_sales(user, obj):
    """Check if user is in sales users for this object."""
    if obj:
        if user in obj.users.all():
            return True
    return True


add_perm('contracts', is_authenticated)
add_perm('contracts.add_contract', is_sales)
add_perm('contracts.view_contract', is_sales | is_support)
add_perm('contracts.change_contract', is_listed_sales)
add_perm('contracts.delete_contract', is_listed_sales)
