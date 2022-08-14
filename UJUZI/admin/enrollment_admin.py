from django.contrib import admin

from ..models import Enrollment


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course','date')
    # search_field = ('name',)

    # def save_model(self, request, obj, form, change):
    #     obj.created_by = request.user
    #     obj.save()


admin.site.register(Enrollment, EnrollmentAdmin)
