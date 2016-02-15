# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buluojianshe', '0006_auto_20160214_0503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='benjamin',
            old_name='maneger',
            new_name='manager',
        ),
    ]
