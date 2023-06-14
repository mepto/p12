from django.contrib.auth.models import AbstractUser, UserManager
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.functions import Lower


class EpicUserManager(UserManager):
    """Extends django user manager for creation methods."""

    def create_user(self, email, password=None, team=None, **extra_fields):
        """Create user and force team information."""
        if not team:
            return ValidationError('No team has been defined. User cannot be created.')
        email = self.normalize_email(email)
        user = User(email=email, team=team, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, team='management', **extra_fields):
        """Create superuser with management team set by default."""
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True

        return self.create_user(email, password, team, **extra_fields)


class User(AbstractUser):
    """Extend django auth user class."""
    TEAM = [
        ('management', 'Management'),
        ('sales', 'Sales'),
        ('support', 'Support'),
    ]
    username = None
    email = models.EmailField(max_length=100, unique=True)
    team = models.CharField(max_length=15, choices=TEAM, blank=False)

    objects = EpicUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['team']

    def __str__(self):
        return self.get_full_name().strip() or self.username

    class Meta:
        app_label = 'epic'
        swappable = "AUTH_USER_MODEL"
        constraints = [
            models.UniqueConstraint(Lower('email'), name='unique_email')
        ]
