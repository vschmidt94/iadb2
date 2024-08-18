from django.contrib import admin
from .models import Department, Person

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_name',)
    search_fields = ('dept_name',)
    list_per_page = 20

@admin.register(Person)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name_first', 'name_last', 'email', 'user_name', 'dept', 'is_active',)
    search_fields = ('name_first', 'name_last', 'user_name')
    list_filter = ('is_active', 'dept')