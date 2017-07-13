# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-13 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic_groups', '0016_academicgroup_exams'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamToAcademicGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_groups.AcademicGroup')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_groups.Exam')),
            ],
        ),
    ]
