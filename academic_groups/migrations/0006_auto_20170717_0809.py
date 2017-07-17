# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-17 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_groups', '0005_auto_20170717_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventgroup',
            name='event_level',
            field=models.CharField(choices=[('m', 'Международный'), ('v', 'Всероссийский'), ('r', 'Региональный'), ('g', 'Городской'), ('u', 'Университетский')], max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='educational_form',
            field=models.CharField(choices=[('b', 'Бюджет'), ('k', 'Контракт')], max_length=1),
        ),
    ]
