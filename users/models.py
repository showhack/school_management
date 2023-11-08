from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, Permission, Group, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from gestion_miembros.models import Persona


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        password_aux = password
        is_market_request = extra_fields.get('is_market_request', False)
        if is_market_request and password is None:
            password_aux = self.make_random_password()
        del extra_fields['is_market_request']
        return self._create_user(email, password=password_aux, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('email address'),
        unique=True,
        blank=True,
        error_messages={'unique': _('There is another user with this email')},
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    first_name = models.CharField(_('First name'), blank=True, max_length=255)
    last_name = models.CharField(_('Last name'), blank=True, max_length=255)

    date_joined = models.DateTimeField(_('Date joined'), default=timezone.now)

    is_rejected = models.BooleanField(
        _('Rejected'),
        default=False,
        help_text=_('Show if the user has been rejected by the staff'),
    )
    rejected_reason = models.CharField(_('Rejected reason'), max_length=256, null=True, blank=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    # Complete Producer Info
    persona = models.OneToOneField(Persona, on_delete=models.RESTRICT, null=True, blank=True)
    user_permissions = models.ManyToManyField(
        Permission, blank=True, related_name='custom_users')
    groups = models.ManyToManyField(
        Group, blank=True, related_name='custom_users')

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('date_joined',)