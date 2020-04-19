from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser


class UserAdmin(BaseUserAdmin):

    list_display = ('email', 'name')
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('personal info', {'fields': ('name',)}),
        ("permissions", {'fields': ("is_staff", "is_superuser")}),
    )
    add_fields = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2')
        })
    )
    search_fields = ('email', )
    ordering = ('email', "name")
    filter_horizontal = ()


admin.site.register(MyUser, UserAdmin)
