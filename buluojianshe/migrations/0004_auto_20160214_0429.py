# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buluojianshe', '0003_auto_20160214_0347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='benjamin',
            options={'verbose_name': '\u677f\u5757', 'verbose_name_plural': '\u677f\u5757'},
        ),
        migrations.RemoveField(
            model_name='benjamin',
            name='sex',
        ),
        migrations.AlterField(
            model_name='benjamin',
            name='creat_timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='benjamin',
            name='last_update_timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='\u66f4\u6539\u65f6\u95f4'),
        ),
    ]
