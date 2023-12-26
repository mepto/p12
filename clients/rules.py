from rules.permissions import add_perm
from rules.predicates import is_authenticated

from users.rules import is_sales, is_support

add_perm('clients', is_authenticated)
add_perm('clients.add_client', is_sales)
add_perm('clients.view_client', is_sales | is_support)
add_perm('clients.change_client', is_sales)
add_perm('clients.delete_client', is_sales)
