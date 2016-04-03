# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='block',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x9d\xbf\xe5\x9d\x97', to='buluojianshe.Benjamin'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u666e\u901a'), (1, '\u6b63\u5e38'), (10, '\u7cbe\u534e')]),
        ),
    ]
