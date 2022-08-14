from django.contrib import admin

from ..models import Course


# class TestInline(admin.TabularInline):
#     form = TForm
#     model = Course
#     fk_name = 'category'

class CourseAdmin(admin.ModelAdmin):
    # form = TForm
    # inlines = [TestInline]
    list_display = ('name','instructor', 'category','image')
    search_field = ('name', 'instructor')


admin.site.register(Course, CourseAdmin)
