from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from rest_framework import status
from ..forms import *


def LoginViewApi(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                data = {
                    "success": "Login Successfully",
                }

                return JsonResponse(data, status=status.HTTP_302_FOUND)

            else:
                data = {
                    "message": "Invalid username or password",
                    "status": "error"
                }

                return JsonResponse(data, status=status.HTTP_302_FOUND)
        else:
            return HttpResponse(form.errors, status=400)

    return render(request, 'UJUZI/student/course_detail.html')


def guest_registration(request):
    if request.POST:
        form = RegisterForm(request.POST)
        print("Post request found")
        if form.is_valid():
            get_user = form.save(commit=False)

            email = form.cleaned_data.get("email")
            phone = form.cleaned_data.get("phone")
            password = form.cleaned_data.get("password")
            password2 = form.cleaned_data.get("password2")

            get_user.email = email
            get_user.phone = phone
            get_user.password = password
            get_user.password2 = password2
            get_user.is_instructor = False

            get_user.save()
            print("Form is valid")
            login(request, get_user)
            data = {
                "success": "Account created and Login Successfully",
            }

            return JsonResponse(data)
        else:
            print(form.errors)
            data = {
                "error": form.errors,
            }

            return JsonResponse(data, status=status.HTTP_302_FOUND)

    return render(request, 'UJUZI/student/course_detail.html')
