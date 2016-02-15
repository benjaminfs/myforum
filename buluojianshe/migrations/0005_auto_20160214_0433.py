# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buluojianshe', '0004_auto_20160214_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benjamin',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u677f\u5757\u540d\u79f0'),
        ),
    ]
