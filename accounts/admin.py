from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Customer, Address


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('created',)


@admin.register(Address)
class AdderssAdmin(admin.ModelAdmin):
    list_display = ('customer',)

UserAdmin.fieldsets[1][1]['fields'] = (
    'first_name',
    'last_name',
    'email',
    # Customer model's custom field
    'phone_number',
)

# Admin can not change user account information
UserAdmin.readonly_fields = (
    'username',
    'first_name',
    'last_name',
    'email',
    'phone_number',
    'last_login',
    'date_joined'
)

UserAdmin.list_display += ('phone_number',)
