from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'user_permissions',
                    'groups',
                )
            },
        ),
        (
            _('Personal info'),
            {
                'fields': (
                    'first_name',
                    'last_name',
                )
            },
        ),
        (
            _('Important dates'),
            {
                'fields': ('date_joined',),
            }
        ),
        (
            _('Profile'),
            {
                'fields': (
                    'is_rejected',
                    'rejected_reason',
                    'persona',
                )
            },
        ),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2')}),
    )
    list_display = (
        'email', 'is_superuser', 'is_active', 'is_staff', 'is_rejected', 'date_joined'
    )
    list_filter = ['is_active', 'is_staff', 'is_superuser', 'groups']
    search_fields = ['email']
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super(UserAdmin, self).get_readonly_fields(request, obj)
        if obj:  # Si estás editando un objeto existente, agrega 'email' a los campos de solo lectura
            readonly_fields += ('email',)
        return readonly_fields

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

    def is_rejected(self, obj):
        return obj.is_rejected

    is_rejected.boolean = True
    is_rejected.short_description = 'Is Rejected'

    def date_joined(self, obj):
        return obj.date_joined

    date_joined.short_description = 'Date Joined'
