# from django.contrib import admin
#
# from ..models import Position
#
#
# class PositionAdmin(admin.ModelAdmin):
#     list_display = ('name', 'created_by')
#     search_field = ('name',)
#
#     def save_model(self, request, obj, form, change):
#         obj.created_by = request.user
#         obj.save()
#
#
# admin.site.register(Position, PositionAdmin)
