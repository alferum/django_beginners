from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.exam_result import Exam_result

def exam_results(request):
    exams = Exam_result.objects.all()
    order_by = request.GET.get('order_by', '')
    if order_by in ('forexam__date', 'forexam__teacher', 'forexam__title', 'forexam__exam_group__title', 'student_name__last_name', 'evaluation'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()
    
    paginator = Paginator(exams, 3)
    page = request.GET.get('page')
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        exams = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        exams = paginator.page(paginator.num_pages)
    
    return render(request, 'students/exam_results.html', {'exams': exams})
