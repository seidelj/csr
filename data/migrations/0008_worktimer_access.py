# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-25 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_eventlog_frame'),
    ]

    operations = [
        migrations.AddField(
            model_name='worktimer',
            name='access',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]