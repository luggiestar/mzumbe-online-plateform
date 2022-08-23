from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..serializers import CourseSerializer
from ..models import Course


class CourseListApi(APIView):
    """api for list of course"""

    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        course = Course.objects.all()
        serializer = self.serializer_class(course, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CourseDetailApi(APIView):
    """api for detail of course"""

    serializer_class = CourseSerializer

    def get_course_object(self, pk):
        return Course.objects.get(pk=pk)

    def get(self, request, pk):
        get_course = self.get_course_object(pk)
        serializer = self.serializer_class(get_course)

        return Response(serializer.data, status=status.HTTP_200_OK)
