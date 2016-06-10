# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20160125_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='teacher',
            field=models.CharField(max_length=128, verbose_name="\u0406\u043c'\u044f \u0432\u0438\u043a\u043b\u0430\u0434\u0430\u0447\u0430"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='title',
            field=models.CharField(max_length=128, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0443'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='exam',
            unique_together=set([('date', 'teacher'), ('title', 'exam_group'), ('date', 'exam_group')]),
        ),
    ]
