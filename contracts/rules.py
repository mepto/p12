import logging

from rules.permissions import add_perm
from rules.predicates import is_authenticated, predicate

from users.models import UserSales, UserSupport


logger = logging.getLogger('main')


@predicate
def is_sales(user, obj):
    """Check if user is in sales."""
    logger.info('[contracts] Can user %s access object %s as sales: %s', user, obj,
                UserSales.objects.filter(user_id=user.id).exists())
    return UserSales.objects.filter(user_id=user.id).exists()


@predicate
def is_support(user, obj):
    """Check if user is in support."""
    logger.info('[contracts] Can user %s access object %s as support: %s', user, obj,
                UserSupport.objects.filter(user_id=user.id).exists())
    return UserSupport.objects.filter(user_id=user.id).exists()


@predicate
def is_listed_sales(user, obj):
    """Check if user is in sales users for this object."""
    if obj and user.id in obj.users.all().values_list('user', flat=True):
        return True
    return False


add_perm('contracts', is_authenticated)
add_perm('contracts.add_contract', is_sales)
add_perm('contracts.view_contract', is_sales | is_support)
add_perm('contracts.change_contract', is_listed_sales)
add_perm('contracts.delete_contract', is_listed_sales)
