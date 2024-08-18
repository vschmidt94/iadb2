from django.contrib import admin
from .models import Process, ProcessComment

class CommentInline(admin.TabularInline):
    model = ProcessComment

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('name', 'note', 'frequency', 'is_active',)
    inlines = [CommentInline,]
    search_fields = ('name',)
    list_filter = ('is_active',)
    list_per_page = 20

@admin.register(ProcessComment)
class ProcessCommentAdmin(admin.ModelAdmin):
    list_display = ('process', 'comment', 'date_created', 'created_by_userid')
    search_fields = ('comment', 'process')
    list_filter = ('process',)
    list_per_page = 30
