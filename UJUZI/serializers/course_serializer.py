from rest_framework import serializers
from ..models import Course, Enrollment, User, Category
from .html_conveter import MLStripper


class CourseSerializer(serializers.ModelSerializer):
    objective = serializers.SerializerMethodField('get_objective')
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.values('name'), many=False)

    class Meta:
        model = Course
        fields = ('id', 'name', 'objective', 'image', 'category')

    def get_objective(self, obj):
        s = MLStripper()
        objective = obj.objective
        s.feed(objective)
        return s.get_data()


class CourserEnrollmentSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=False)
    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)

    class Meta:
        model = Enrollment
        fields = ('student', 'course')
