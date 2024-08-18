"""
Registers Auditor Models with Django Admin module
"""
from django.contrib import admin

from .models import AuditorRole, Auditor

class AuditorAdmin(admin.ModelAdmin):
    list_display = ('name_last', 'name_first', 'is_active')
    search_fields = ('name_last', 'name_first')
    list_filter = ('roles', 'is_active')
    list_per_page = 20

# Register your models here.
admin.site.register(Auditor, AuditorAdmin)
admin.site.register(AuditorRole)
