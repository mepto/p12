from django.db import models


class UppercaseField(models.CharField):

    def get_prep_value(self, value):
        return str(value).upper()


class CapitalizeField(models.CharField):

    def get_prep_value(self, value):
        return str(value).capitalize()


class LowercaseEmailField(models.EmailField):

    def get_prep_value(self, value):
        return str(value).lower()
