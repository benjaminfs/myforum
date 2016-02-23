# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buluojianshe', '0007_auto_20160215_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300, verbose_name='\u6587\u7ae0\u540d')),
                ('content', models.CharField(max_length=10000, verbose_name='\u6587\u7ae0\u5185\u5bb9')),
                ('status', models.IntegerField(verbose_name='\u72b6\u6001', choices=[(0, '\u666e\u901a'), (1, '\u6b63\u5e38'), (10, '\u7cbe\u534e')])),
                ('creat_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(auto_now=True)),
                ('block', models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x9d\xbf\xe5\x9d\x97', to='buluojianshe.Benjamin')),
                ('owner', models.ForeignKey(verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
    ]
