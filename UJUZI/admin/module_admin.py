from django.contrib import admin

from ..models import Module


class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title','course', 'content', 'created_by')
    search_field = ('title','course')


admin.site.register(Module, ModuleAdmin)
