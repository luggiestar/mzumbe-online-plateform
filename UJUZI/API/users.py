from django.contrib.auth import authenticate, login
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..serializer import UserLoginSerializer


class UserSignUpApi(APIView):
    """Api for user signup"""
    serializer_class = UserLoginSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'msg': 'success',
                'data': serializer.data
            }

            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {
                'msg': serializer.errors
            }
            return Response(response, status=status.HTTP_200_OK)


class UserSignIn(APIView):
    """Api for user signin"""
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            response = {
                'msg':'success',
                'token': user.auth_token.key,
                'user_id': user.id
            }

            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'msg': 'Invalid username or password',
            }

            return Response(response, status=status.HTTP_200_OK)
