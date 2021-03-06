# Generated by Django 3.1.2 on 2021-03-12 19:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0004_auto_20210312_0101'),
    ]

    operations = [
        migrations.CreateModel(
            name='check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done', models.CharField(choices=[(1, 'Утечка персональных данных'), (2, 'Утечка фото/видео'), (3, 'Распространение секретных данных')], max_length=100, null=True)),
                ('source', models.CharField(max_length=100)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('kursant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='space.all_kursants')),
            ],
        ),
    ]
