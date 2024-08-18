from django.contrib import admin
from .models import Standard, Requirement

@admin.register(Standard)
class StandardAdmin(admin.ModelAdmin):
    list_display = ('name', 'revision', 'is_active', 'description')

@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'standard', 'coverage_by', 'description', 'note', 'is_active' )
    search_fields = ('identifier', 'description')
    list_filter = ('standard', 'coverage_by', 'date_created')
    list_per_page = 20