# Generated by Django 3.1.2 on 2021-07-03 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0008_auto_20210317_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='kursant',
        ),
        migrations.RemoveField(
            model_name='kursant_fail',
            name='kursant',
        ),
        migrations.DeleteModel(
            name='tasks',
        ),
        migrations.DeleteModel(
            name='tasks_bad',
        ),
        migrations.DeleteModel(
            name='tasks_good',
        ),
        migrations.DeleteModel(
            name='all_kursants',
        ),
        migrations.DeleteModel(
            name='check',
        ),
        migrations.DeleteModel(
            name='kursant_fail',
        ),
    ]