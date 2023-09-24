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


add_perm('epic', is_authenticated)

add_perm('epic.add_statuscontract', is_sales)
add_perm('epic.view_statuscontract', is_sales | is_support)
add_perm('epic.change_statuscontract', is_sales)
add_perm('epic.delete_statuscontract', is_sales)

add_perm('epic.add_statusevent', is_sales)
add_perm('epic.view_statusevent', is_sales | is_support)
add_perm('epic.change_statusevent', is_sales | is_support)
add_perm('epic.delete_statusevent', is_sales)
