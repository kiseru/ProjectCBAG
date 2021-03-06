# Generated by Django 2.2.4 on 2019-08-16 19:38
from django.db import migrations

groups = ['headman', 'jury']


def initialize_groups_forward(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    for group in groups:
        Group.objects.create(name=group)


def initialize_groups_backward(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name__in=groups).delete()


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.RunPython(initialize_groups_forward, initialize_groups_backward)
    ]
