from django.conf.global_settings import MEDIA_ROOT
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages


from ..forms import *
from ..models import *


def instructor_home(request):
    get_user = get_object_or_404(Staff, user=request.user)
    get_course = Course.objects.filter(instructor=get_user)
    count = Course.objects.filter(instructor=get_user).count()
    form = CourseForm(request.POST)
    if request.POST:
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.instructor = get_user
            save_form.save()

            if save_form:
                messages.success(request, f"Course added successfully.")
                return redirect('UJUZI:instructor_home')
    else:
        form = CourseForm()

    context = {
        'course': get_course,
        'count': count,
        'form': form,

    }
    return render(request, 'user/instructor_home.html', context)


def update_course(request, object_pk):
    try:
        instance = Course.objects.get(id=object_pk)
    except Course.DoesNotExist:
        instance = None
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('UJUZI:instructor_home')
    else:
        form = CourseForm(instance=instance)
    context_dict = {'form': form, 'instance': instance}
    return render(request, 'user/edit_course.html', context_dict)


def update_module(request, object_pk, course):
    get_course = get_object_or_404(Course, name=course)

    try:
        instance = Module.objects.get(id=object_pk)
    except Course.DoesNotExist:
        instance = None
    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('UJUZI:course_module', course=get_course.name)
    else:
        form = ModuleForm(instance=instance)
    context_dict = {'form': form, 'instance': instance}
    return render(request, 'user/edit_module_content.html', context_dict)


def update_module_content(request, object_pk, module, course):
    get_course = get_object_or_404(Course, name=course)

    get_module = get_object_or_404(Module, name=module)
    try:
        instance = Content.objects.get(id=object_pk)
    except Course.DoesNotExist:
        instance = None
    if request.method == 'POST':
        form = ContentForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('UJUZI:module_content', course=get_course.name, module=get_module.name)
    else:
        form = ContentForm(instance=instance)
    context_dict = {'form': form, 'instance': instance}
    return render(request, 'user/edit_module_content.html', context_dict)


def course_module(request, course):
    get_user = get_object_or_404(Staff, user=request.user)
    get_status = get_object_or_404(Status, code="REV")

    get_course = get_object_or_404(Course, name=course)
    get_module = Module.objects.filter(course=get_course)
    count_module = Module.objects.filter(course=get_course).count
    count = Content.objects.filter(module__id__in=Module.objects.values('id')).values('module',
                                                                                      'module__id', ).annotate(
        total=Count('module__id')).order_by('total')

    check_reverted = Verification.objects.filter(status=get_status, content__module__course=get_course).count()

    if request.POST:
        form = ModuleForm(request.POST)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.created_by = request.user
            save_form.course = get_course
            save_form.save()

            if save_form:
                messages.success(request, f"Module added successfully.")
                return redirect('UJUZI:course_module', course=course)
    else:
        form = ModuleForm()

    context = {
        'module': get_module,
        'course': get_course,
        'count': count,
        'check': check_reverted,
        'form': form,
        'count_module': count_module,
        'attrs': None, 'renderer': None

    }
    return render(request, 'user/course_module.html', context)




def pdf_view(request, content):
    get_content = get_object_or_404(Content, title=content)
    with open(f'{get_content.file.url}', 'r') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response


@login_required
def my_course(request):
    try:
        get_course = Course.objects.filter(instructor=request.user)
        get_course_total = Course.objects.filter(instructor=request.user).count()
    except:
        get_course = None
        get_course_total = 0
    context = {
        'courses': get_course,
        'total': get_course_total,

    }
    return render(request, 'UJUZI/tutor/my_course.html', context)
