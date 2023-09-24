from django.contrib import admin
from django.contrib.auth.models import Group
from rules.contrib.admin import ObjectPermissionsModelAdmin

from epic.models import StatusContract, StatusEvent


class StatusEventAdmin(ObjectPermissionsModelAdmin):
    """Allow event status class for rules."""


class StatusContractAdmin(ObjectPermissionsModelAdmin):
    """Allow contract status class for rules."""


admin.site.unregister(Group)
admin.site.register(StatusEvent)
admin.site.register(StatusContract)
