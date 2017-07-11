# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-11 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_groups', '0009_auto_20170711_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='student',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_event_group',
        ),
        migrations.AddField(
            model_name='event',
            name='student_event',
            field=models.ManyToManyField(to='academic_groups.Student'),
        ),
    ]
