# Generated by Django 2.2.4 on 2019-08-17 05:34

from django.db import migrations, models
from django.db.models import F


def transfer_value(apps, schema_editor):
    EventGroup = apps.get_model('academic_groups', 'EventGroup')
    for event_group in EventGroup.objects.all():
        event_group.prize_winning_place_temp = int(event_group.prize_winning_place)
        event_group.save()


class Migration(migrations.Migration):

    dependencies = [
        ('academic_groups', '0007_remove_student_average_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventgroup',
            name='prize_winning_place_temp',
            field=models.PositiveSmallIntegerField(choices=[(1, '1 место'), (2, '2 место'), (3, '3 место'), (0, 'участие')], default=0),
            preserve_default=False,
        ),
        migrations.RunPython(transfer_value, lambda x, y: x),
        migrations.RemoveField(
            model_name='eventgroup',
            name='prize_winning_place'
        ),
        migrations.RenameField(
            model_name='eventgroup',
            old_name='prize_winning_place_temp',
            new_name='prize_winning_place'
        )
    ]
