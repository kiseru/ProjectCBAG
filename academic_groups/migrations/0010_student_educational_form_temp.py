# Generated by Django 2.2.4 on 2019-08-17 06:26

from django.db import migrations, models

educational_from_mapping = ['b', 'k']


def forward(apps, schema_editor):
    Student = apps.get_model('academic_groups', 'Student')
    for student in Student.objects.all():
        student.educational_form_temp = educational_from_mapping.index(student.educational_form)
        student.save()


def backward(apps, schema_editor):
    Student = apps.get_model('academic_groups', 'Student')
    for student in Student.objects.all():
        student.educational_form = educational_from_mapping[student.educational_form_temp]
        student.save()


class Migration(migrations.Migration):
    dependencies = [
        ('academic_groups', '0009_auto_20190817_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='educational_form_temp',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Бюджет'), (1, 'Контракт')], default=0),
            preserve_default=False,
        ),
        migrations.RunPython(forward, backward),
        migrations.RemoveField(
            model_name='student',
            name='educational_form'
        ),
        migrations.RenameField(
            model_name='student',
            old_name='educational_form_temp',
            new_name='educational_form'
        )
    ]