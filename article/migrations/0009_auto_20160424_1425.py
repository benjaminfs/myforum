# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20160423_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='block',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x9d\xbf\xe5\x9d\x97', to='buluojianshe.Benjamin'),
        ),
    ]
