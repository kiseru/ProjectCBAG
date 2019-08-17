# Generated by Django 2.2.4 on 2019-08-17 06:13

from django.db import migrations, models

event_area_mapping = ['n', 'k', 's', 'o']
event_level_mapping = ['m', 'v', 'r', 'g', 'u']


def transfer_event_group_values_forward(apps, schema_editor):
    EventGroup = apps.get_model('academic_groups', 'EventGroup')
    for event_group in EventGroup.objects.all():
        event_group.event_area_temp = event_area_mapping.index(event_group.event_area)
        event_group.event_level_temp = event_level_mapping.index(event_group.event_level)


def transfer_event_group_values_backward(apps, schema_editor):
    EventGroup = apps.get_model('academic_groups', 'EventGroup')
    for event_group in EventGroup.objects.all():
        event_group.event_area = event_area_mapping[event_group.event_area_temp]
        event_group.event_level = event_level_mapping[event_group.event_level_temp]


class Migration(migrations.Migration):
    dependencies = [
        ('academic_groups', '0008_eventgroup_prize_winning_place_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventgroup',
            name='event_area_temp',
            field=models.PositiveSmallIntegerField(
                choices=[(0, 'Научная'), (1, 'Культурная'), (2, 'Спортивная'), (4, 'Общественная')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventgroup',
            name='event_level_temp',
            field=models.PositiveSmallIntegerField(
                choices=[(0, 'Международный'), (1, 'Всероссийский'), (2, 'Региональный'), (3, 'Городской'),
                         (4, 'Университетский')], default=0),
            preserve_default=False,
        ),
        migrations.RunPython(transfer_event_group_values_forward, transfer_event_group_values_backward),
        migrations.RemoveField(
            model_name='eventgroup',
            name='event_level'
        ),
        migrations.RenameField(
            model_name='eventgroup',
            old_name='event_level_temp',
            new_name='event_level'
        ),
        migrations.RemoveField(
            model_name='eventgroup',
            name='event_area'
        ),
        migrations.RenameField(
            model_name='eventgroup',
            old_name='event_area_temp',
            new_name='event_area'
        )
    ]
