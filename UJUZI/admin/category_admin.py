from django.contrib import admin

from ..models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_field = ('name',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


admin.site.register(Category, CategoryAdmin)
# admin.site.register(Author)
# admin.site.register(Entry)
