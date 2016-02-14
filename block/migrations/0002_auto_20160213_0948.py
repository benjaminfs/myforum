# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demo',
            name='last_ypdate_timestamp',
        ),
        migrations.AddField(
            model_name='demo',
            name='last_update_timestamp',
            field=models.DateField(default=datetime.datetime(2016, 2, 13, 9, 48, 46, 934502), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='demo',
            name='create_timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
