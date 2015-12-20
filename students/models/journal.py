# -*- coding: utf-8 -*-

from django.db import models

class Journal(models.Model):
    """Journal Model"""
    
    class Meta(object):
        verbose_name = u"Журнал відвідування"
        verbose_name_plural = u"Журнали відвідування"
    
    student_name = models.ForeignKey('Student', verbose_name=u"Студент")
    
    d1 = models.BooleanField(default=False, verbose_name = u'Ср 1')
    d2 = models.BooleanField(default=False, verbose_name = u'Чт 2')
    d3 = models.BooleanField(default=False, verbose_name = u'Пт 3')
    d4 = models.BooleanField(default=False, verbose_name = u'Сб 4')
    d5 = models.BooleanField(default=False, verbose_name = u'Нд 5')
    d6 = models.BooleanField(default=False, verbose_name = u'Пн 6')
    d7 = models.BooleanField(default=False, verbose_name = u'Вт 7')
    d8 = models.BooleanField(default=False, verbose_name = u'Ср 8')
    d9 = models.BooleanField(default=False, verbose_name = u'Чт 9')
    d10 = models.BooleanField(default=False, verbose_name = u'Пт 10')
    d11 = models.BooleanField(default=False, verbose_name = u'Сб 11')
    d12 = models.BooleanField(default=False, verbose_name = u'Нд 12')
    d13 = models.BooleanField(default=False, verbose_name = u'Пн 13')
    d14 = models.BooleanField(default=False, verbose_name = u'Вт 14')
    d15 = models.BooleanField(default=False, verbose_name = u'Ср 15')
    d16 = models.BooleanField(default=False, verbose_name = u'Чт 16')
    d17 = models.BooleanField(default=False, verbose_name = u'Пт 17')
    d18 = models.BooleanField(default=False, verbose_name = u'Сб 18')
    d19 = models.BooleanField(default=False, verbose_name = u'Нд 19')
    d20 = models.BooleanField(default=False, verbose_name = u'Пн 20')
    d21 = models.BooleanField(default=False, verbose_name = u'Вт 21')
    d22 = models.BooleanField(default=False, verbose_name = u'Ср 22')
    d23 = models.BooleanField(default=False, verbose_name = u'Чт 23')
    d24 = models.BooleanField(default=False, verbose_name = u'Пт 24')
    d25 = models.BooleanField(default=False, verbose_name = u'Сб 25')
    d26 = models.BooleanField(default=False, verbose_name = u'Нд 26')
    d27 = models.BooleanField(default=False, verbose_name = u'Пн 27')
    d28 = models.BooleanField(default=False, verbose_name = u'Вт 28')
    d29 = models.BooleanField(default=False, verbose_name = u'Ср 29')
    d30 = models.BooleanField(default=False, verbose_name = u'Чт 30')
    d31 = models.BooleanField(default=False, verbose_name = u'Пт 31')
    
    def __unicode__(self):
        return u"%s %s" % (self.student_name.first_name, self.student_name.last_name)

#import datetime
#datetime.date(2015, 12, 14).weekday()

#import calendar
#[i for i in calendar.Calendar().itermonthdays2(2015, 12) if i[0]]
#days = {0: u"Пн", 1: u"Вт", 2: u"Ср", 3: u"Чт", 4: u"Пт", 5: u"Сб", 6: u"Нд"}
