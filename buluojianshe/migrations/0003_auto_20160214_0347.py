# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('buluojianshe', '0002_auto_20160213_1305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='benjamin',
            options={'verbose_name': '\u6a21\u5757', 'verbose_name_plural': '\u6a21\u5757'},
        ),
        migrations.RenameField(
            model_name='benjamin',
            old_name='owner',
            new_name='maneger',
        ),
        migrations.RenameField(
            model_name='benjamin',
            old_name='user_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='benjamin',
            name='user_num',
        ),
        migrations.AddField(
            model_name='benjamin',
            name='desc',
            field=models.CharField(default=datetime.datetime(2016, 2, 14, 3, 47, 33, 547484), max_length=300, verbose_name='\u63cf\u8ff0'),
            preserve_default=False,
        ),
    ]
