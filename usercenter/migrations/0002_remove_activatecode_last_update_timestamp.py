# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercenter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activatecode',
            name='last_update_timestamp',
        ),
    ]
