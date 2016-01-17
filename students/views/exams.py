# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from django.forms import ModelForm
from django.views.generic import CreateView, UpdateView, DeleteView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, HTML
from crispy_forms.bootstrap import FormActions

from ..models.exam import Exam

class ExamCreateForm(ModelForm):
    class Meta:
        model = Exam
    
    def __init__(self, *args, **kwargs):
        super(ExamCreateForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        
        # set form tag attributes
        self.helper.form_action = reverse('exams_add')
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        
        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'
        
        # add buttons
        self.helper.layout.append(FormActions(
            Div(css_class = self.helper.label_class),
            Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
            HTML(u"<a class='btn btn-link' name='cancel_button' href='{% url 'exams' %}?status_message=Додавання/редагування іспиту скасовано!'>Скасувати</a>"),
        ))

class ExamUpdateForm(ExamCreateForm):

    def __init__(self, *args, **kwargs):
        super(ExamUpdateForm, self).__init__(*args, **kwargs)
        self.helper.form_action = reverse('exams_edit', kwargs = {'pk': kwargs['instance'].id})

class ExamCreateView(CreateView):
    model = Exam
    template_name = 'students/exams_edit.html'
    form_class = ExamCreateForm
    
    def get_success_url(self):
        messages.success(self.request, u'Іспит %s успішно додано!' % self.object)
        return reverse('exams')

class ExamUpdateView(UpdateView):
    model = Exam
    template_name = 'students/exams_edit.html'
    form_class = ExamUpdateForm
    
    def get_success_url(self):
        messages.success(self.request, u'Іспит %s успішно збережено!' % self.object)
        return reverse('exams')

class ExamDeleteView(DeleteView):
    model = Exam
    template_name = 'students/exams_confirm_delete.html'
    
    def get_success_url(self):
        messages.success(self.request, u'Іспит %s успішно видалено!' % self.object)
        return reverse('exams')

def exams_list(request):
    exams = Exam.objects.all()
    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'date', 'teacher', 'exam_group'):
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
    
    return render(request, 'students/exams.html', {'exams': exams})
