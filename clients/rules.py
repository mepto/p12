from rules.permissions import add_perm
from rules.predicates import is_authenticated, predicate

import logging

from users.models import UserSales, UserSupport


logger = logging.getLogger('main')


@predicate
def is_sales(user, obj):
    """Check if user is in sales."""
    logger.info('[clients] Can user %s access object %s as sales: %s', user, obj,
                UserSales.objects.filter(user_id=user.id).exists())
    return UserSales.objects.filter(user_id=user.id).exists()


@predicate
def is_support(user, obj):
    """Check if user is in support."""
    logger.info('[clients] Can user %s access object %s as support: %s', user, obj,
                UserSupport.objects.filter(user_id=user.id).exists())
    return UserSupport.objects.filter(user_id=user.id).exists()


add_perm('clients', is_authenticated)
add_perm('clients.add_client', is_sales)
add_perm('clients.view_client', is_sales | is_support)
add_perm('clients.change_client', is_sales)
add_perm('clients.delete_client', is_sales)
