from django.apps import AppConfig


class EpicConfig(AppConfig):
    """Configure app settings."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'epic'
    verbose_name = "Epic Events"
