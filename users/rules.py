from rules.permissions import add_perm
from rules.predicates import is_authenticated, predicate

from users.models import UserManagement, UserSales, UserSupport


@predicate
def is_management(user, obj):
    """Check if user is in management."""
    return UserManagement.objects.filter(user_id=user.id).exists()


@predicate
def is_sales(user, obj):
    """Check if user is in sales."""
    return UserSales.objects.filter(user_id=user.id).exists()


@predicate
def is_support(user, obj):
    """Check if user is in support."""
    return UserSupport.objects.filter(user_id=user.id).exists()


@predicate
def themselves(user, obj):
    """Check if user is trying to change themselves."""
    return user == obj


add_perm('users', is_authenticated)
add_perm('users.add_user', is_management)
add_perm('users.view_user', is_management | is_sales | is_support)
add_perm('users.change_user', is_management & ~themselves)
add_perm('users.delete_user', is_management & ~themselves)

add_perm('users.add_usermanagement', is_management)
add_perm('users.view_usermanagement', is_management | is_sales | is_support)
add_perm('users.change_usermanagement', is_management & ~themselves)
add_perm('users.delete_usermanagement', is_management & ~themselves)

add_perm('users.add_usersales', is_management)
add_perm('users.view_usersales', is_management | is_sales | is_support)
add_perm('users.change_usersales', is_management)
add_perm('users.delete_usersales', is_management)

add_perm('users.add_usersupport', is_management)
add_perm('users.view_usersupport', is_management | is_sales | is_support)
add_perm('users.change_usersupport', is_management)
add_perm('users.delete_usersupport', is_management)
