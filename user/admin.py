from django.contrib import admin

from .models import UserDetails


class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")
    search_fields = ("id", "name", "email")


admin.site.register(UserDetails, UserDetailsAdmin)
