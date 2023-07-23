from django.db import models

from epic.classes import CapitalizeField


class StatusContract(models.Model):
    """Store status for contracts."""

    name = CapitalizeField(max_length=25, blank=True)

    def __str__(self):
        """Default human-readable return for contract status object."""
        return self.name


class StatusEvent(models.Model):
    """Store status for events."""

    name = CapitalizeField(max_length=25, blank=True)

    def __str__(self):
        """Default human-readable return for event status object."""
        return self.name
