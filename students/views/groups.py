# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def groups_list(request):
    groups = (
        {'id': 1, 'title': 'МтМ-21', 'leader': u'Ячменев Олег'},
        {'id': 2, 'title': 'МтМ-22', 'leader': u'Віталій Подоба'},
        {'id': 3, 'title': 'МтМ-23', 'leader': u'Іванов Андрій'},
        )
    return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
