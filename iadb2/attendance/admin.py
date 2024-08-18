"""
Register Attendance Models with Djanfo Admin module.

.. Todo::
    * Time picker in admin module needs better choices than noon, 6, etc
"""
from django.contrib import admin
from .models import Event, AttendanceRecord


class EventAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'event_type', 'duration_min', 'allow_checkin')
    list_filter = ('event_type', )
    date_hierarchy = ('date_time')
    search_fields = ('event_desc', 'notes')
    list_per_page = 20


# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(AttendanceRecord)
