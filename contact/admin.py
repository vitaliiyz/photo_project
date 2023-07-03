from django.contrib import admin
from contact.models import Contact


class AdminContact(admin.ModelAdmin):
    last_display = ("name", "status", "updated")


admin.site.register(Contact, AdminContact)
