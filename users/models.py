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
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create superuser with management team set by default."""
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Extend django auth user class."""
    username = models.CharField(max_length=150, unique=True)
    email = LowercaseEmailField(max_length=320, unique=True)
    last_name = UppercaseField(max_length=150, blank=True)
    first_name = CapitalizeField(max_length=150, blank=True)
    date_modified = models.DateTimeField(auto_now=True)
    objects = EpicUserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        """Default human-readable return for base user object."""
        return self.get_full_name().strip() or self.email

    class Meta:
        """Meta class."""
        verbose_name = 'User (base)'
        verbose_name_plural = 'Users (base)'
        swappable = 'AUTH_USER_MODEL'
        constraints = [
            models.UniqueConstraint(Lower('email'), name='unique_email')
        ]


class UserManagement(models.Model):
    """Store Management users."""
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        """Default human-readable return for user management object."""
        return self.user.get_full_name().strip() or self.user.email

    class Meta:
        """Meta class."""
        verbose_name = 'User (management)'
        verbose_name_plural = 'Users (management)'


class UserSupport(models.Model):
    """Store Support users."""
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        """Default human-readable return for user support object."""
        return self.user.get_full_name().strip() or self.user.email

    class Meta:
        """Meta class."""
        verbose_name = 'User (support)'
        verbose_name_plural = 'Users (support)'


class UserSales(models.Model):
    """Store Sales users."""
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        """Default human-readable return for user sales object."""
        return self.user.get_full_name().strip() or self.user.email

    class Meta:
        """Meta class."""
        verbose_name = 'User (sales)'
        verbose_name_plural = 'Users (sales)'
