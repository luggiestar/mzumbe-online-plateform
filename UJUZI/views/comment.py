from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.core import serializers
import json

from ..models import *


def commentView(request):
    list_of_comment = Comment.objects.all()
    module_of_list = Module.objects.all()

    context = {
        'list_of_comment': list(list_of_comment),
        'module_of_list': module_of_list,
    }

    return render(request, 'user/comments.html', context)


def listComment(request):
    response_data = {}
    list_of_comment = Comment.objects.all()
    list_two = []
    for i in list_of_comment:
        list_two.append([i.convo, i.enrollment.student.user.email, i.enrollment.student.user.first_name,
                         i.enrollment.student.user.last_name, i.enrollment.student.user.id])

    response_data = list(list_two)
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def saveCommentView(request):
    if request.method == "POST":
        convo = request.POST.get("convo")
        module = request.POST.get("module")
        get_user = request.user
        get_moudule = get_object_or_404(Module, id=module)
        get_enrollment = get_object_or_404(Enrollment, student__user=get_user)

        Comment.objects.create(
            convo=convo,
            module=get_moudule,
            enrollment=get_enrollment
        )

        return redirect('UJUZI:list_of_comment')
# return render(request, 'ELP/comment.html', context)
