from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.core import serializers
import json

from django.template.loader import render_to_string

from ..forms import RequestForm
from ..models import *


def base_view(request):
    return render(request, 'UJUZI/base.html')


def home_view(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        artists = Course.objects.filter(name__icontains=url_parameter)
        total = Course.objects.filter(name__icontains=url_parameter).count()
        count = "1"

    else:
        artists = None
        count = None
        total = None

    does_req_accept_json = request.accepts("application/json")
    is_ajax_request = request.headers.get("x-requested-with") == "XMLHttpRequest" and does_req_accept_json

    if is_ajax_request:
        html = render_to_string(
            template_name="UJUZI/search-results-partial.html",
            context={"artists": artists, "total": total, "count": count}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    category = Category.objects.all()

    course = Course.objects.all()
    latest = Course.objects.all().order_by('-id')[:2]
    context = {
        'courses': course,
        'categories': category,
        'latest': latest,
        'artists': artists,
        'count': count
    }
    return render(request, 'UJUZI/home.html', context)


def course_detail(request, course_name):
    check_course = get_object_or_404(Course, name=course_name)
    try:
        get_enroll = Enrollment.objects.filter(student=request.user, course=check_course).first()
    except:
        get_enroll = None
    modules = Module.objects.filter(course=check_course)
    total = Module.objects.filter(course=check_course).count()
    context = {
        'courses': check_course,
        'modules': modules,
        'total': total,
        'enrolled': get_enroll,

    }
    return render(request, 'UJUZI/student/course_detail.html', context)

@login_required
def module_content(request, module_id):
    check_module = get_object_or_404(Module, id=module_id)
    context = {
        'module': check_module,

    }
    return render(request, 'UJUZI/student/course_content.html', context)

@login_required
def course_enrollment(request, course_id):
    get_course = get_object_or_404(Course, id=course_id)
    save_enrollment = Enrollment.objects.create(student=request.user, course=get_course)

    return redirect('UJUZI:course_detail', course_name=get_course.name)

@login_required
def enrolled_course(request):
    try:
        get_enroll = Enrollment.objects.filter(student=request.user)
        get_enroll_total = Enrollment.objects.filter(student=request.user).count()
    except:
        get_enroll = None
        get_enroll_total = 0
    context = {
        'enrollment': get_enroll,
        'total': get_enroll_total,

    }
    return render(request, 'UJUZI/student/enrolled_course.html', context)

@login_required
def teaching_request(request):

    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.tutor = request.user

            save_form.save()
            return redirect('UJUZI:teaching_request',)
    else:
        form = RequestForm()

    return render(request, 'UJUZI/student/teaching_request.html', {'form':form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('UJUZI:change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'UJUZI/student/change_password.html', {
        'form': form
    })




