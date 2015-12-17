# -*- coding: utf-8 -*-

from django.db import models

class Exam(models.Model):
    """Exam Model"""
    
    class Meta(object):
        verbose_name = u"Іспит"
        verbose_name_plural = u"Іспити"
        
    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва предмету")
        
    date = models.DateTimeField(
        blank=False,
        verbose_name=u"Дата і час проведення",
        null=True)
        
    teacher = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Ім'я викладача")
        
    exam_group = models.ForeignKey('Group',
        verbose_name=u"Група",
        blank=False,
        null=True)
    def __unicode__(self):
        return u"%s %s" % (self.exam_group.title, self.title)
