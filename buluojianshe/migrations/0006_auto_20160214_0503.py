# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buluojianshe', '0005_auto_20160214_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benjamin',
            name='last_update_timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4'),
        ),
    ]
