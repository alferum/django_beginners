# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from django.forms import ModelForm
from django.views.generic import CreateView, UpdateView, DeleteView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, HTML
from crispy_forms.bootstrap import FormActions

from ..models.groups import Group
from ..util import paginate


class GroupCreateForm(ModelForm):
    class Meta:
        model = Group
    
    def __init__(self, *args, **kwargs):
        super(GroupCreateForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        
        # set form tag attributes
        self.helper.form_action = reverse('groups_add')
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
            HTML(u"<a class='btn btn-link' name='cancel_button' href='{% url 'groups' %}?status_message=Додавання/редагування групи скасовано!'>Скасувати</a>"),
        ))
        # blank field leader in form create group
        self.fields['leader'].queryset = self.fields['leader'].queryset.none()

class GroupUpdateForm(GroupCreateForm):

    def __init__(self, *args, **kwargs):
        super(GroupUpdateForm, self).__init__(*args, **kwargs)
        self.helper.form_action = reverse('groups_edit', kwargs = {'pk': kwargs['instance'].id})
        # filter students from current group
        self.fields['leader'].queryset = self.instance.student_set.order_by('last_name')
        
class GroupCreateView(CreateView):
    model = Group
    template_name = 'students/groups_edit.html'
    form_class = GroupCreateForm
    
    def get_success_url(self):
        messages.success(self.request, u'Групу %s успішно додано!' % self.object.title)
        return reverse('groups')

class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'students/groups_edit.html'
    form_class = GroupUpdateForm
    
    def form_valid(self, form):
        leader = form.cleaned_data['leader']
        #field blank or leader's group == current group
        if not leader or leader.student_group == self.object:
            return super(GroupUpdateView, self).form_valid(form)
        else:
            messages.error(self.request, u'Студент належить до іншої групи.')
            return super(GroupUpdateView, self).form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, u'Групу %s успішно збережено!' % self.object.title)
        return reverse('groups')
        
class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/groups_confirm_delete.html'
    
    def delete(self, request, *args, **kwargs):
        """Delete if group is empty"""
        group = self.get_object()
        # if group is empty
        if group.student_set.exists():
            messages.error(self.request, u'Помилка. Група %s не порожня.' % group.title)
        else:
            group.delete()
            messages.success(self.request, u'Групу успішно видалено!')
        return HttpResponseRedirect(reverse('groups'))

def groups_list(request):
    groups = Group.objects.all()
    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader__last_name'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()
    
    context = paginate(groups, 3, request, {}, var_name='groups')
    return render(request, 'students/groups_list.html', context)
