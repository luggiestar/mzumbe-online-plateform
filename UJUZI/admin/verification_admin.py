from django.contrib import admin

from ..models import TeachingRequest,CourseSummary


class VerificationAdmin(admin.ModelAdmin):
    list_display = ('tutor', 'institution', 'letter','is_verified')
    search_field = ('tutor')


admin.site.register(TeachingRequest, VerificationAdmin)
admin.site.register(CourseSummary)
