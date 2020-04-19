from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser
from django.utils.translation import gettext as _


class UserAdmin(BaseUserAdmin):

    list_display = ('email', 'name')
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name',)}),
        (_("Permissions"), {'fields': ("is_staff", "is_superuser")}),
        (_('Dates'), {'fields': ('last_login', )})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    search_fields = ('email', )
    ordering = ('id', )
    filter_horizontal = ()


admin.site.register(MyUser, UserAdmin)
