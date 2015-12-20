# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam_result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evaluation', models.IntegerField(verbose_name='\u041e\u0446\u0456\u043d\u043a\u0430')),
                ('forexam', models.ForeignKey(verbose_name='\u0406\u0441\u043f\u0438\u0442', to='students.Exam', null=True)),
                ('student_name', models.ForeignKey(verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442', to='students.Student', null=True)),
            ],
            options={
                'verbose_name': '\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0456\u0441\u043f\u0438\u0442\u0443',
                'verbose_name_plural': '\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0438 \u0456\u0441\u043f\u0438\u0442\u0456\u0432',
            },
            bases=(models.Model,),
        ),
    ]
