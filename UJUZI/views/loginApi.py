from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView


def LoginViewApi(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                response = {
                    "success": "Login Successfully",
                }

                return JsonResponse(response, status=status.HTTP_302_FOUND)

            else:
                response = {
                    "message": "Invalid username or password",
                    "status": "error"
                }

                return JsonResponse(response, status=status.HTTP_302_FOUND)
        else:
            return HttpResponse(form.errors, status=400)

    return render(request, 'ELP/login.html')


class LoginApi(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:
            response = {
                "message": "Login successfully"
            }

            return Response(response, status=status.HTTP_302_FOUND)
        response = {
            "message": "Invalid username or password"
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
