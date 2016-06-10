# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from django.forms import ModelForm
from django.views.generic import UpdateView, DeleteView, CreateView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, HTML #, Layout, Field, Fieldset
from crispy_forms.bootstrap import FormActions, AppendedText

from ..models.students import Student
from ..models.groups import Group
from ..util import paginate, get_current_group


class StudentCreateForm(ModelForm):
    class Meta:
        model = Student
    
    def __init__(self, *args, **kwargs):
        super(StudentCreateForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        
        # set form tag attributes
        self.helper.form_action = reverse('students_add')
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        
        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        
        self.helper['birthday'].wrap(AppendedText, '<i class="glyphicon glyphicon-calendar"></i>')
        #self.helper.layout[3] = AppendedText('birthday', '<i class="glyphicon glyphicon-calendar"></i>')
        
        # add buttons
        self.helper.layout.append(HTML(
            u'<div class="form-group"><label class="col-sm-2 control-label"></label><div class="controls col-sm-10">\
            <input class="btn btn-primary" type="submit" value="Зберегти" name="add_button">\
            <a class="btn btn-link" href="/?status_message=Додавання/редагування студента скасовано!" name="cancel_button">Скасувати</a></div></div>'))

        #self.helper.layout.append(Div(
        #    Div(css_class = self.helper.label_class),
        #    Div(Submit('add_button', u'Зберегти'),
        #        HTML(u"<a class='btn btn-link' name='cancel_button' href='{% url 'home' %}?status_message=Додавання/редагування студента скасовано!'>Скасувати</a>"),
        #        css_class = 'controls col-sm-10'),
        #    css_class = 'form-group'))

class StudentUpdateForm(StudentCreateForm):

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)
        self.helper.form_action = reverse('students_edit', kwargs = {'pk': kwargs['instance'].id})
        group = self.instance.student_group
        if group and group.leader == self.instance:
            # filter groups for field if current student is leader current group
            self.fields['student_group'].queryset = Group.objects.filter(leader=self.instance)

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentUpdateForm
    
    def get_success_url(self):
        return u'%s?status_message=Студента %s %s успішно збережено!' % (reverse('home'), self.object.first_name, self.object.last_name)
        
    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=Редагування студента відмінено!' % reverse('home'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        """Check if student is leader in any group. If yes, then ensure it's the same as selected group."""
        # get group where current student is a leader
        group = Group.objects.filter(leader=self.object.id)
        group = None
        if group and form.cleaned_data['student_group'] != group:
            messages.error(self.request, u'Студент є старостою групи %s.' % group.title)
            return super(StudentUpdateView, self).form_invalid(form)
        else:
            return super(StudentUpdateView, self).form_valid(form)

class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentCreateForm
    
    def get_success_url(self):
        messages.info(self.request, u'Студента %s %s успішно додано!' % (self.object.first_name, self.object.last_name))
        return reverse('home')
        
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/students_confirm_delete.html'
    
    def get_success_url(self):
        return u'%s?status_message=Студента успішно видалено!' % reverse('home')

def students_list(request):
    # check if we need to show only one group of students
    current_group = get_current_group(request)
    if current_group:
        students = Student.objects.filter(student_group=current_group)
    else:
        # otherwise show all students
        students = Student.objects.all()
    
    # try to order students list
    #order_by = request.GET.get('order_by', 'last_name') # default sorted by last_name
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()
    
    # apply pagination, 3 students per page
    context = paginate(students, 3, request, {}, var_name='students')
    return render(request, 'students/students_list.html', context)

def students_add(request):
    # was form posted?
    if request.method == "POST":
        # was form add button clicked?
        if request.POST.get('add_button') is not None:
            # errors collection
            errors = {}
            
            # data for student object
            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}
                    
            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u"Ім'я є обов'язковим"
            else:
                data['first_name'] = first_name
                
            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u"Прізвище є обов'язковим"
            else:
                data['last_name'] = last_name
                
            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u"Дата народження є обов'язковою"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = u"Введіть коректний формат дати (напр. 1984-12-30)"
                else:
                    data['birthday'] = birthday
                
            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u"Номер білета є обов'язковим"
            else:
                data['ticket'] = ticket
                
            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u"Оберіть групу для студента"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Оберіть коректну групу"
                else:
                    data['student_group'] = groups[0]
                
            photo = request.FILES.get('photo')
            if photo:
                if photo.size > 1024 * 1024 * 2:
                    errors['student_photo'] = u"Розмір файлу більший 2 мегабайт (%s байт). " % photo.size
                if photo.content_type not in ['image/jpeg', 'image/png']:
                    errors['student_photo'] += u"Допустимі типи файлів jpeg, jpg, png."
                data['photo'] = photo
                
            # save student
            if not errors:
                student = Student(**data)
                student.save()
                
                # redirect to students list
                messages.success(request, u'Студента %s %s успішно додано!' % (first_name, last_name))
                return HttpResponseRedirect(reverse('home'))
                
            else:
                # render form with errors and previous user input
                messages.error(request, u'Будь-ласка, виправте наступні помилки')
                return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title'), 'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            messages.info(request, u'Додавання студента скасовано!')
            return HttpResponseRedirect(reverse('home'))
    else:
        # initial form render
        return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title')})
