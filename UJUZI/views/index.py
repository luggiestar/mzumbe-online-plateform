from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core import serializers
import json

from django.template.loader import render_to_string
from django.views.generic import DetailView

from django.views.generic import DetailView, ListView

from ..forms import *
from ..models import Course


def index(request):
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
    latest = Course.objects.all().order_by('-id')[:3]
    context = {
        'courses': course,
        'categories': category,
        'latest': latest,
        'artists': artists,
        'count': count
    }

    return render(request, 'ELP/index.html', context)


# def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))


def registration(request):
    if request.POST:
        form = RegisterForm(request.POST)

        if form.is_valid():
            get_user = form.save(commit=False)
            get_user.is_instructor = False
            get_user.save()
            login(request, get_user)
            # Student.objects.create(user=get_user, code=id_generator())
            return redirect('UJUZI:home_view')

    else:
        form = RegisterForm()

    context = {

        'form': form,

    }
    return render(request, 'ELP/registration.html', context)


def user_profile(request, object_pk):
    try:
        instance = User.objects.get(id=object_pk)
    except User.DoesNotExist:
        instance = None
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('UJUZI:user_profile', object_pk=instance.id)
    else:
        form = ProfileForm(instance=instance)
    context_dict = {'form': form, 'instance': instance}
    return render(request, 'UJUZI/student/user_profile.html', context_dict)


def RegisterView(request):
    form = CourseForm
    return render(request, 'ELP/registration/register.html', {'form': form})


def browseCourseView(request):
    list_of_course = Course.objects.all()
    categories = Category.objects.all()
    context = {
        'list_of_course': list_of_course,
        'categories': categories
    }
    return render(request, 'ELP/browseCourse.html', context)


class CourseItemView(DetailView):
    model = Course
    template_name = 'ELP/courseItem.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = Module.objects.all()
        return context
