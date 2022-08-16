from django.conf.global_settings import MEDIA_ROOT
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages

from ..forms import *
from ..models import *


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






def pdf_view(request, content):
    get_content = get_object_or_404(Module, title=content)
    with open(f'{get_content.file.url}', 'r') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response


@login_required
def my_course(request):
    try:
        get_course = Course.objects.filter(instructor=request.user)
        get_course_total = Course.objects.filter(instructor=request.user).count()
        # get_enrollments_total = Enrollment.objects.filter(course=get_course).count()
    except:
        get_course = None
        get_course_total = 0
        # get_enrollments_total = 0

    form = CourseForm()

    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            save_form = form.save(commit=False)

            save_form.instructor = request.user

            save_form.save()

            return redirect('UJUZI:course_module_contents', course_id=save_form.id)
    context = {

        'courses': get_course,
        'total': get_course_total,
        # 'enrollment': get_enrollments_total,
        'form': form,

    }
    return render(request, 'UJUZI/tutor/my_course.html', context)


@login_required
def course_module_contents(request, course_id):
    try:

        get_course = Course.objects.filter(id=course_id).first()
        get_module = Module.objects.filter(course=get_course)
        total = Module.objects.filter(course=get_course).count()
    except:
        get_course = None
        get_module = None
        total = 0

    form = ModuleForm()

    if request.method == "POST":
        form = ModuleForm(request.POST, request.FILES)
        if form.is_valid():
            save_form = form.save(commit=False)

            save_form.created_by = request.user
            save_form.course = get_course

            save_form.save()

            return redirect('UJUZI:course_module_contents', course_id=course_id)
    context = {

        'courses': get_course,
        'modules': get_module,
        'total': total,
        'form': form,

    }
    return render(request, 'UJUZI/tutor/course_module_contents.html', context)



def update_module_content(request, object_pk):

    get_module = get_object_or_404(Module, id=object_pk)
    try:
        instance = Module.objects.get(id=object_pk)
    except Course.DoesNotExist:
        instance = None
    if request.method == 'POST':
        form = ModuleForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('UJUZI:course_module_contents', course_id=get_module.course.id)
    else:
        form = ModuleForm(instance=instance)
    context = {'form': form, 'instance': instance}
    return render(request, 'UJUZI/tutor/edit_module.html', context)

def delete_module(request, module_id):
    get_content = Module.objects.filter(id=module_id).first()
    get_course = get_content.course.id
    get_content.delete()

    # messages.success(request, 'Deleted successfully')

    return redirect('UJUZI:course_module_contents', course_id=get_course)