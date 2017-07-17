# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-17 08:07
from __future__ import unicode_literals

import academic_groups.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_groups', '0004_eventgroup_academic_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicgroup',
            name='starosta_phone_number',
            field=models.CharField(max_length=12, validators=[academic_groups.models.validate_telephone_number]),
        ),
        migrations.AlterField(
            model_name='eventgroup',
            name='event_level',
            field=models.CharField(choices=[('m', 'Международный'), ('v', 'Всероссийский'), ('r', 'Региональный'), ('g', 'Городской'), ('u', 'Университетский')], max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='educational_form',
            field=models.CharField(choices=[('b', 'Бюджет'), ('k', 'Контракт')], max_length=8),
        ),
    ]
