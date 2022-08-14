from django.conf.global_settings import MEDIA_ROOT
from django.db import transaction
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core import serializers
import json

from django.views.generic import DetailView, ListView

from ..forms import *
from ..models import *


def verifier_home(request):
    get_user = get_object_or_404(Staff, user=request.user)
    get_course = Verification.objects.filter(status__code="REQ").values('content__module__course__name',
                                                                        'content__module__course__modules',
                                                                        'content__module__course__instructor__user__email',
                                                                        'content__module__course__instructor__institution__name').distinct()
    get_module = Verification.objects.filter(status__code="REQ").values('content__module__course__name',
                                                                        'content__module__name').distinct()

    context = {
        'course': get_course,
        'module': get_module,

    }
    return render(request, 'user/course_verification.html', context)


def verify_staff(request):
    get_user = get_object_or_404(Staff, user=request.user)
    get_staff = Staff.objects.filter(is_verified=False)

    context = {
        'staff': get_staff,

    }
    return render(request, 'user/staff_verification.html', context)


def accept_verification(request, staff_code):
    get_staff = get_object_or_404(Staff, id=staff_code)
    update_user = User.objects.filter(id=get_staff.user.id).first()
    update_user.is_tutor = True
    update_user.save()

    return redirect('UJUZI:verify_staff',)

def course_content(request, course):
    get_user = get_object_or_404(Staff, user=request.user)
    get_status = get_object_or_404(Status, code="REQ")

    get_course = get_object_or_404(Course, name=course)
    # get_module = Module.objects.filter(course=get_course)
    count = Verification.objects.filter(content__module__course=get_course, status=get_status).order_by('content')
    form = RevertForm()
    context = {
        'content': count,
        'form': form,

    }
    return render(request, 'user/course_contents.html', context)


def content_verification(request, contents):
    get_content = get_object_or_404(Verification, id=contents)
    get_status = get_object_or_404(Status, code="APP")
    get_user = get_object_or_404(Staff, user=request.user)
    # with transaction.atomic():
    #     cards = Verification.objects.select_for_update().filter(
    #         id=get_content.id
    #     )[:1]
    #     if cards:
    check_verification = Verification.objects.get(id=get_content.id)
    check_verification.verifier = request.user
    check_verification.status = get_status
    check_verification.save()
    Content.objects.filter(id=get_content.content.id).update(is_valid=True)

    return redirect('UJUZI:course_contents', course=get_content.content.module.course.name)


def content_verification_revert(request, contents):
    get_content = get_object_or_404(Verification, id=contents)
    get_status = get_object_or_404(Status, code="REV")
    get_user = get_object_or_404(Staff, user=request.user)
    if request.method == 'POST':
        form = RevertForm(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['reason']
            check_verification = Verification.objects.get(id=get_content.id)
            check_verification.verifier = request.user
            check_verification.status = get_status
            check_verification.reason = reason
            check_verification.save()

    return redirect('UJUZI:course_contents', course=get_content.content.module.course.name)

# def course_content_verification(request, content):
#     get_user = get_object_or_404(Staff, user=request.user)
#
#     get_course = get_object_or_404(Course, name=course)
#     # get_module = Module.objects.filter(course=get_course)
#     count =Content.objects.filter(module__course=get_course).order_by('module')
#
#
#     context = {
#         'content': count,
#
#     }
#     return render(request, 'user/course_contents.html', context)

#
# def module_contents(request, course, module):
#     get_course = get_object_or_404(Course, name=course)
#
#     get_module = get_object_or_404(Module, name=module)
#     get_content = Content.objects.filter(module=get_module)
#     count_content = Content.objects.filter(module=get_module).count()
#
#     form = ContentForm(request.POST, request.FILES)
#     if request.POST:
#         if form.is_valid():
#             save_form = form.save(commit=False)
#             save_form.created_by = request.user
#             save_form.module = get_module
#             save_form.save()
#
#             if save_form:
#                 messages.success(request, f"content added successfully.")
#                 return redirect('UJUZI:module_content', course=course, module=module)
#     else:
#         form = ContentForm()
#
#     context = {
#         'content': get_content,
#         'module': get_module.name,
#         'form': form,
#         'course': get_course.name,
#         'count': count_content,
#
#     }
#     return render(request, 'user/module_contents.html', context)
