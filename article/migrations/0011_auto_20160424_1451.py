# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20160424_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='block',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u677f\u5757', to='buluojianshe.Benjamin'),
        ),
        migrations.AlterField(
            model_name='article',
            name='owner',
            field=models.ForeignKey(verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL),
        ),
    ]
