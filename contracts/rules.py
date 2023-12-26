from rules.permissions import add_perm
from rules.predicates import is_authenticated, predicate

from users.rules import is_sales, is_support


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
