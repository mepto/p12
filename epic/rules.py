from rules.permissions import add_perm
from rules.predicates import is_authenticated, predicate

from users.rules import is_sales, is_support

add_perm('epic', is_authenticated)

add_perm('epic.add_statuscontract', is_sales)
add_perm('epic.view_statuscontract', is_sales | is_support)
add_perm('epic.change_statuscontract', is_sales)
add_perm('epic.delete_statuscontract', is_sales)

add_perm('epic.add_statusevent', is_sales)
add_perm('epic.view_statusevent', is_sales | is_support)
add_perm('epic.change_statusevent', is_sales | is_support)
add_perm('epic.delete_statusevent', is_sales)
