from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.core import serializers
import json

from django.template.loader import render_to_string

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
    modules = Module.objects.filter(course=check_course)
    total = Module.objects.filter(course=check_course).count()
    context = {
        'courses': check_course,
        'modules': modules,
        'total': total,

    }
    return render(request, 'UJUZI/student/course_detail.html', context)


def module_content(request, module_id):
    check_module = get_object_or_404(Module, id=module_id)
    context = {
        'module': check_module,

    }
    return render(request, 'UJUZI/student/course_content.html', context)


def profile_view(request):
    return render(request, 'UJUZI/student/user_profile.html')


def teaching_request(request):
    return render(request, 'UJUZI/student/teaching_request.html')
def change_password(request):
    return render(request, 'UJUZI/student/change_password.html')


def get_course(request, id):
    course = Course.objects.filter(category__id=id)

    get_course_list = serializers.serialize('json', course)

    return JsonResponse(get_course_list, safe=False)
