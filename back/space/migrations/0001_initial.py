# Generated by Django 3.1.2 on 2021-03-10 22:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='all_kursants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fakultet', models.IntegerField()),
                ('kurs', models.IntegerField()),
                ('narushen', models.IntegerField(default=8)),
                ('fix', models.IntegerField(default=5)),
                ('teach_group', models.CharField(default='671/11', max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('otchestvo', models.CharField(default='Петрович', max_length=100)),
                ('charact', models.CharField(default='Исполнительный курсант, не склонен к нарушениям. Уровень доверия высокий. Рекомендуем к работе в ЗГТ.', max_length=5000)),
                ('rank', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Источник', 'Источник'), ('Факультет', 'Факультет'), ('Курсант', 'Курсант')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tasks_good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='space.tasks')),
            ],
        ),
        migrations.CreateModel(
            name='tasks_bad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='space.tasks')),
            ],
        ),
        migrations.CreateModel(
            name='kursant_fail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done', models.CharField(choices=[(1, 'Утечка персональных данных'), (2, 'Утечка фото/видео'), (3, 'Распространение секретных данных')], max_length=100, null=True)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('kursant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='space.all_kursants')),
            ],
        ),
    ]
