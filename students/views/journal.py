# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def journal(request):
    students = (
        {'id': 1, 's_name': u'Подоба Віталій'},
        {'id': 2, 's_name': u'Корост Андрій'},
        {'id': 3, 's_name': u'Притула Тарас'},
        )
    days = ['Ср 1', 'Чт 2', 'Пт 3', 'Сб 4', 'Нд 5', 'Пн 6', 'Вт 7', 'Ср 8', 'Чт 9', 'Пт 10', 'Сб 11', 'Нд 12', 'Пн 13', 'Вт 14', 'Ср 15', 'Чт 16', 
            'Пт 17', 'Сб 18', 'Нд 19', 'Пн 20', 'Вт 21', 'Ср 22', 'Чт 23', 'Пт 24', 'Сб 25', 'Нд 26', 'Пн 27', 'Вт 28', 'Ср 29', 'Чт 30', 'Пт 31']
    return render(request, 'students/journal.html', {'students': students, 'days': days})
    
def journal_edit(request, sid):
    return HttpResponse('<h1>Edit Journal %s</h1>' % sid)
