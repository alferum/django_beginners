from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.journal import Journal

def journal(request):
  
    journals = Journal.objects.all()
    checks = journals.values_list()
    if checks: 
        checks = [i[2:] for i in checks]
    journals = zip(journals, checks)
    
    paginator = Paginator(journals, 3)
    page = request.GET.get('page')
    try:
        journals = paginator.page(page)
    except PageNotAnInteger:
        journals = paginator.page(1)
    except EmptyPage:
        journals = paginator.page(paginator.num_pages)
    
    dates = [field.verbose_name for field in Journal._meta.fields[2:]]
    
    return render(request, 'students/journal.html', {'journals': journals, 'dates': dates })
    
def journal_edit(request, sid):
    return HttpResponse('<h1>Edit Journal %s</h1>' % sid)
