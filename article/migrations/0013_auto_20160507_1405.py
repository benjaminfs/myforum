# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20160424_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='block',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u677f\u5757', to='buluojianshe.Benjamin'),
        ),
    ]
