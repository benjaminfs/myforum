# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buluojianshe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='benjamin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=50, verbose_name='\u7528\u6236\u540d')),
                ('user_num', models.IntegerField(verbose_name='\u7528\u6236\u4ee3\u78bc')),
                ('sex', models.IntegerField(verbose_name='\u6027\u5225', choices=[(1, '\u7537'), (2, '\u5973')])),
                ('creat_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_register',
            name='owner',
        ),
        migrations.DeleteModel(
            name='user_register',
        ),
    ]
