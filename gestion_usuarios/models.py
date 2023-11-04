from django.db import models
from gestion_miembros.models import (Persona)
from django.contrib.auth.models import (AbstractUser, Permission, Group)


class CustomPermission(Permission):
    category = models.CharField(max_length=255)


class Roles(Group):
    permiso = models.ManyToManyField(
        Permission, through='RelacionCustomPermissionRoles')


class RelacionCustomPermissionRoles(models.Model):
    permiso = models.ForeignKey(
        CustomPermission, on_delete=models.SET_NULL, null=True, blank=True, to_field='name')
    rol = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True)


class CustomUser(AbstractUser):
    persona = models.OneToOneField(Persona, on_delete=models.RESTRICT)
    rol = models.ManyToManyField(Roles, through='CustomUserRelacionRoles')


class CustomUserRelacionRoles(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, blank=True, to_field='username')
    rol = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True)
