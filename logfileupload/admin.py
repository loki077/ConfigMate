from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from django.db import models

# Extend the existing UserAdmin to add extra fields in the admin interface
class UserAdmin(BaseUserAdmin):
    # Add additional list display fields
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    # If you have a custom user model with additional fields:
    # fieldsets = BaseUserAdmin.fieldsets + (
    #     ('Additional Info', {'fields': ('custom_field',)}),
    # )

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # Add other fields as needed

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Product)