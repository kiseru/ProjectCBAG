# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-11 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic_groups', '0005_auto_20170711_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curator',
            name='academic_group',
        ),
        migrations.AddField(
            model_name='academicgroup',
            name='curator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='academic_groups.Curator'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='academicgroup',
            name='starosta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_groups.Student', unique=True),
        ),
    ]
