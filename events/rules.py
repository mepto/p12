from dateutil.utils import today
from rules.permissions import add_perm
from rules.predicates import is_authenticated, predicate

from users.rules import is_sales, is_support


@predicate
def date_is_passed(user, obj):
    """Check if item date is in the past."""
    try:
        return obj.event_date < today().date()
    except AttributeError:
        return False


@predicate
def is_listed_support(user, obj):
    """Check if user is in support users for the object."""
    if obj and user.id in obj.users.all().values_list('user', flat=True):
        return True
    return False


add_perm('events', is_authenticated)
add_perm('events.add_event', is_sales)
add_perm('events.view_event', is_support | is_sales)
add_perm('events.change_event', (is_support & ~date_is_passed & is_listed_support))
add_perm('events.delete_event', (is_support & ~date_is_passed & is_listed_support))
