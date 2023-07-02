from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models.functions import Lower

from epic.classes import CapitalizeField, LowercaseEmailField, UppercaseField


class EpicUserManager(UserManager):
    """Extends django user manager for creation methods."""

    def create_user(self, email, password=None, **extra_fields):
        """Create user and force team information."""
        email = self.normalize_email(email)
        user = User(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create superuser with management team set by default."""
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Extend django auth user class."""
    username = None
    email = LowercaseEmailField(max_length=100, unique=True)
    last_name = UppercaseField(max_length=150, blank=True)
    first_name = CapitalizeField(max_length=150, blank=True)
    date_modified = models.DateTimeField(auto_now=True)
    objects = EpicUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.get_full_name().strip() or self.username

    class Meta:
        verbose_name = "User (base)"
        verbose_name_plural = "Users (base)"
        app_label = 'epic'
        swappable = "AUTH_USER_MODEL"
        constraints = [
            models.UniqueConstraint(Lower('email'), name='unique_email')
        ]


class UserManagement(models.Model):
    """Store Management users."""
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)


class UserSupport(models.Model):
    """Store Support users."""
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)


class UserSales(models.Model):
    """Store Sales users."""
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
