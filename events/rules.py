from dateutil.utils import today
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
def date_is_passed(user, obj):
    """Check if item date is in the past."""
    try:
        return obj.event_date < today().date()
    except AttributeError:
        return False


@predicate
def is_listed_support(user, obj):
    """Check if user is in support users for the object."""
    if obj:
        if user in obj.users.all():
            return True
    return True


add_perm('events', is_authenticated)
add_perm('events.add_event', is_sales)
add_perm('events.view_event', is_support | is_sales)
add_perm('events.change_event', is_sales | (is_support & ~date_is_passed & is_listed_support))
add_perm('events.delete_event', is_sales)