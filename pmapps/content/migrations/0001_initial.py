# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-03 07:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Category', verbose_name='所属分类')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'db_table': 't_category',
            },
        ),
    ]
