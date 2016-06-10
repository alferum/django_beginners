# -*- coding: utf-8 -*-

from django.db import models

class Exam_result(models.Model):
    """Exam Model"""
    
    class Meta(object):
        verbose_name = u"Результат іспиту"
        verbose_name_plural = u"Результати іспитів"
        unique_together = ('forexam', 'student_name')
        
    forexam = models.ForeignKey('Exam',
        verbose_name=u"Іспит",
        blank=False,
        null=True)
        
    student_name = models.ForeignKey('Student',
        verbose_name=u"Студент",
        blank=False,
        null=True)
        
    evaluation = models.PositiveSmallIntegerField(
        verbose_name=u"Оцінка")
        
    def __unicode__(self):
        #return u"%s %s %s" % (self.student_name, self.forexam.title, self.evaluation)
        return u"%s %s %s" % (self.student_name, self.forexam.title, self.forexam.id)

#foo = models.ForeignKey('Exam', to_field='exam_group')
#foo2 = models.ForeignKey('Student', to_field='student_group')
#unique_together = ('foo', 'student_name')
