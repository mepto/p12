from django.db import models


class UppercaseField(models.CharField):
    """MAke a field uppercase."""
    def get_prep_value(self, value):
        """Catch value before database save."""
        return str(value).upper()


class CapitalizeField(models.CharField):
    """Make a field capitalized."""
    def get_prep_value(self, value):
        """Catch value before database save."""
        return str(value).capitalize()


class LowercaseEmailField(models.EmailField):
    """Make a field lowercase."""
    def get_prep_value(self, value):
        """Catch value before database save."""
        return str(value).lower()
