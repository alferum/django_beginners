# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_student_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('d1', models.BooleanField(default=False, verbose_name='\u0421\u0440 1')),
                ('d2', models.BooleanField(default=False, verbose_name='\u0427\u0442 2')),
                ('d3', models.BooleanField(default=False, verbose_name='\u041f\u0442 3')),
                ('d4', models.BooleanField(default=False, verbose_name='\u0421\u0431 4')),
                ('d5', models.BooleanField(default=False, verbose_name='\u041d\u0434 5')),
                ('d6', models.BooleanField(default=False, verbose_name='\u041f\u043d 6')),
                ('d7', models.BooleanField(default=False, verbose_name='\u0412\u0442 7')),
                ('d8', models.BooleanField(default=False, verbose_name='\u0421\u0440 8')),
                ('d9', models.BooleanField(default=False, verbose_name='\u0427\u0442 9')),
                ('d10', models.BooleanField(default=False, verbose_name='\u041f\u0442 10')),
                ('d11', models.BooleanField(default=False, verbose_name='\u0421\u0431 11')),
                ('d12', models.BooleanField(default=False, verbose_name='\u041d\u0434 12')),
                ('d13', models.BooleanField(default=False, verbose_name='\u041f\u043d 13')),
                ('d14', models.BooleanField(default=False, verbose_name='\u0412\u0442 14')),
                ('d15', models.BooleanField(default=False, verbose_name='\u0421\u0440 15')),
                ('d16', models.BooleanField(default=False, verbose_name='\u0427\u0442 16')),
                ('d17', models.BooleanField(default=False, verbose_name='\u041f\u0442 17')),
                ('d18', models.BooleanField(default=False, verbose_name='\u0421\u0431 18')),
                ('d19', models.BooleanField(default=False, verbose_name='\u041d\u0434 19')),
                ('d20', models.BooleanField(default=False, verbose_name='\u041f\u043d 20')),
                ('d21', models.BooleanField(default=False, verbose_name='\u0412\u0442 21')),
                ('d22', models.BooleanField(default=False, verbose_name='\u0421\u0440 22')),
                ('d23', models.BooleanField(default=False, verbose_name='\u0427\u0442 23')),
                ('d24', models.BooleanField(default=False, verbose_name='\u041f\u0442 24')),
                ('d25', models.BooleanField(default=False, verbose_name='\u0421\u0431 25')),
                ('d26', models.BooleanField(default=False, verbose_name='\u041d\u0434 26')),
                ('d27', models.BooleanField(default=False, verbose_name='\u041f\u043d 27')),
                ('d28', models.BooleanField(default=False, verbose_name='\u0412\u0442 28')),
                ('d29', models.BooleanField(default=False, verbose_name='\u0421\u0440 29')),
                ('d30', models.BooleanField(default=False, verbose_name='\u0427\u0442 30')),
                ('d31', models.BooleanField(default=False, verbose_name='\u041f\u0442 31')),
                ('students', models.ForeignKey(verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0438', to='students.Student')),
            ],
            options={
                'verbose_name': '\u0412\u0456\u0434\u0432\u0456\u0434\u0443\u0432\u0430\u043d\u043d\u044f',
                'verbose_name_plural': '\u0412\u0456\u0434\u0432\u0456\u0434\u0443\u0432\u0430\u043d\u043d\u044f',
            },
            bases=(models.Model,),
        ),
    ]
