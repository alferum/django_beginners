# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_journal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='journal',
            options={'verbose_name': '\u0416\u0443\u0440\u043d\u0430\u043b \u0432\u0456\u0434\u0432\u0456\u0434\u0443\u0432\u0430\u043d\u043d\u044f', 'verbose_name_plural': '\u0416\u0443\u0440\u043d\u0430\u043b\u0438 \u0432\u0456\u0434\u0432\u0456\u0434\u0443\u0432\u0430\u043d\u043d\u044f'},
        ),
        migrations.RenameField(
            model_name='journal',
            old_name='students',
            new_name='student_name',
        ),
    ]
