from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from ..forms import CourseSearchForm, Course
from ..models import *


# def profile_view(request):
#     get_enrollement = Enrollment.objects.filter(student__user=request.user)
#     get_module = Module.objects.all()
#     enrollment_count = Enrollment.objects.filter(student__user=request.user).count()
#     form2 = CourseSearchForm()
#     if request.is_ajax():
#         term = request.GET.get('term')
#         courses = Course.objects.all().filter(name__icontains=term)
#         response_content = list(courses.values())
#         return JsonResponse(response_content, safe=False)
#
#     # form = StaffForm(request.POST)
#     if request.POST:
#         if form.is_valid():
#             save_form = form.save(commit=False)
#             save_form.user = request.user
#             save_form.save()
#
#             if save_form:
#                 messages.success(request, f"requested successfully.")
#                 return redirect('UJUZI:profile')
#     else:
#         form = StaffForm()
#     context = {
#         'form2': form2,
#         'form': form,
#         'enrollment': get_enrollement,
#         'count': enrollment_count,
#         'staff': get_staff,
#         'module': get_module
#
#     }
#
#     return render(request, "user/profile.html", context)


def course_details(request):
    form = CourseSearchForm()
    if request.GET:
        get_course__name = request.GET.get('course')
        get_course = Course.objects.filter(id=get_course__name).first()
        get_module = Module.objects.filter(course__id=get_course__name)
        # get_content = Content.objects.filter(module__course__id=get_course__name)
        try:
            get_status = Enrollment.objects.filter(student__user=request.user, course=get_course)
        except:
            get_status = None

        context = {
            # 'content': get_content,
            'module': get_module,
            'course': get_course,
            'form': form,
            'status': get_status,

        }

        return render(request, "user/course_detail.html", context)
    else:
        context = {

            'form': form,

        }
        return render(request, "user/course_detail.html", context)


def detailed_course(request, code):
    get_course = Course.objects.filter(name=code).first()
    get_module = Module.objects.filter(course=get_course)
    # get_content = Content.objects.filter(module__course=get_course)
    try:
        get_status = Enrollment.objects.filter(student__user=request.user, course=get_course)
    except:
        get_status = None

    context = {
        # 'content': get_content,
        'module': get_module,
        'course': get_course,
        'status': get_status,

    }

    return render(request, "user/detailed_course.html", context)


def get_module_contents(request, module_name):
    get_module = get_object_or_404(Module, name=module_name)
    # get_content = Content.objects.filter(module=get_module)
    # count_content = Content.objects.filter(module=get_module).count()

    context = {
        # 'content': get_content,
        'module': get_module,
        # 'count': count_content,

    }
    return render(request, 'user/module_content_details.html', context)
