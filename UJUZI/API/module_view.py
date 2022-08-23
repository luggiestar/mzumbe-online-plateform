from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..models import Module, Course
from ..serializers import ModuleSerializer


class CourseModule(APIView):
    def get_course_object(self, course):
        return Course.objects.filter(pk=course).first()

    def get(self, request, course):
        get_course = self.get_course_object(course)
        module = Module.objects.filter(course=get_course)
        serializer = ModuleSerializer(module, many=True)
        response = {
            "data": serializer.data
        }
        return Response(response)
