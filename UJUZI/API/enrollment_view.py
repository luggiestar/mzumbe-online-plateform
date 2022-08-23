from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..serializers import CourseSerializer, CourserEnrollmentSerializer
from ..models import Course, User, Enrollment


class CourseEnrollApi(APIView):
    """api for course enrolled of course"""

    serializer_course_class = CourseSerializer
    serializer_enrollment_class = CourserEnrollmentSerializer

    def get_course_object(self, pk):
        return Course.objects.get(pk=pk)

    def get_user_object(self, user):
        return User.objects.filter(pk=user).first()

    def get_enrollemnt_object(self, user, pk):
        return Enrollment.objects.filter(student=user, course=pk).first()

    def get(self, request, pk, user_id):
        get_user = self.get_user_object(user_id)
        get_enroll = self.get_enrollemnt_object(get_user, pk)
        serializer = self.serializer_enrollment_class(get_enroll)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_enrollment_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "msg": "Enrolled successfully"
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                "msg": "Something went wrong try again"
            }
            return Response(response, status=status.HTTP_200_OK)
