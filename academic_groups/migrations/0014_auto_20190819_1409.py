# Generated by Django 2.2.4 on 2019-08-19 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academic_groups', '0013_academicgroupexam'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='academicgroupexam',
            unique_together={('academic_group', 'exam')},
        ),
    ]