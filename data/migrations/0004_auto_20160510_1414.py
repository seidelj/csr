# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-10 19:14
from __future__ import unicode_literals

import data.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20160510_1325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventlog',
            options={'ordering': ['timestamp']},
        ),
        migrations.AddField(
            model_name='treatment',
            name='assignment',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='batch',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='frameorder',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='timestarted',
            field=models.DateTimeField(default=data.models.get_now),
        ),
    ]
