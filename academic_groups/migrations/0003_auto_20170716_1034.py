# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-16 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_groups', '0002_auto_20170716_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventgroup',
            name='event_area',
            field=models.CharField(choices=[('n', 'Научная'), ('k', 'Культурно-массовая'), ('s', 'Спортивная'), ('o', 'Общественная')], max_length=1),
        ),
        migrations.AlterField(
            model_name='eventgroup',
            name='event_level',
            field=models.CharField(choices=[('ml', 'Международный'), ('rl', 'Всероссийский'), ('rl', 'Региональный'), ('gl', 'Городской'), ('ul', 'Университетский')], max_length=2),
        ),
        migrations.AlterField(
            model_name='eventgroup',
            name='prize_winning_place',
            field=models.CharField(choices=[('0', 'участие'), ('1', '1 место'), ('2', '2 место'), ('3', '3 место')], max_length=1),
        ),
        migrations.AlterField(
            model_name='eventgroup',
            name='student_event',
            field=models.ManyToManyField(blank=True, to='academic_groups.Student'),
        ),
    ]
