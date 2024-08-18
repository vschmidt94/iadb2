"""
Audits app - admin module
"""

from django.contrib import admin
from .models import AuditPeriod, AuditTemplate
from iadb2 import requirements, processes


@admin.register(AuditPeriod)
class AuditPeriodAdmin(admin.ModelAdmin):
    list_display = ('year', 'type', 'period', 'date_start', 'date_end')
    list_filter = ('year',)
    list_per_page = 20


@admin.register(AuditTemplate)
class AuditTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'for_process', 'note', 'is_active')
    search_fields = ('for_process', 'requirements', 'note')
    list_filter = ('is_active', 'for_process', 'requirements',)
    list_per_page = 20

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Limit the choices to only active processes.
        """
        if db_field.name == "for_process":
            kwargs["queryset"] = processes.models.Process.objects.filter(
                is_active=True)
        return super(AuditTemplateAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        """
        Limit the choice for requirements in Admin interface to
        only active requirements with 'self' coverage
        """
        if db_field.name == "requirements":
            cov_filter = 'S'    # S = Self-coverage
            act_filter = True   # Only Active Requrements
            kwargs["queryset"] = (
                requirements.models.Requirement.objects.filter(
                    coverage_by=cov_filter, is_active=act_filter))
        return (super(AuditTemplateAdmin, self)
                .formfield_for_manytomany(db_field, request, **kwargs))
