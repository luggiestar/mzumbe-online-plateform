from django.contrib import admin

from ..models import Institution


class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)

    search_field = ('name',)



admin.site.register(Institution, InstitutionAdmin)
