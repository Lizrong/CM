# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-04 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='账户')),
                ('password', models.CharField(max_length=100, verbose_name='口令')),
                ('nickname', models.CharField(max_length=50, verbose_name='昵称')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('photo', models.CharField(blank=True, max_length=100, verbose_name='头像')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 't_user',
            },
        ),
    ]
