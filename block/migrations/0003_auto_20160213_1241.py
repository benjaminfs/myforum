# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0002_auto_20160213_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo',
            name='example4char',
            field=models.CharField(max_length=30, verbose_name='\u5b57\u7b26\u7bc4\u4f8b'),
        ),
        migrations.AlterField(
            model_name='demo',
            name='example4int',
            field=models.IntegerField(verbose_name='\u6578\u5b57\u7bc4\u4f8b'),
        ),
        migrations.AlterField(
            model_name='demo',
            name='sex',
            field=models.IntegerField(verbose_name='\u6027\u5225', choices=[(1, '\u7537'), (2, ' \u5973')]),
        ),
    ]
