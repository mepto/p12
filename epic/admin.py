from django.contrib import admin
from epic.models.user import User


class EpicAdminSite(admin.AdminSite):
    site_header = "Epic Events administration"


admin_site = EpicAdminSite(name="Epic Events administration")
admin_site.register(User)
