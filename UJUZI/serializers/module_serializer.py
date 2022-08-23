from rest_framework import serializers
from ..models import Module


class ModuleSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name', read_only=True)
    course_id = serializers.CharField(source='course.id', read_only=True)
    instructor = serializers.CharField(source='created_by.email', read_only=True)

    class Meta:
        model = Module
        fields = ('title', 'content', 'extension', 'course_name', 'instructor', 'uploaded_date', 'uploaded_time', 'course_id')
