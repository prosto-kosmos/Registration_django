# Generated by Django 2.2.7 on 2021-06-04 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20210423_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('entity_id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Идентификатор объекта')),
                ('visibility', models.BooleanField(default=True, verbose_name='Отображение указателя')),
                ('shown_param', models.BooleanField(default=False, verbose_name='Отображение списка параметров')),
                ('shown_preview', models.BooleanField(default=False, verbose_name='Отображение окна с превью')),
                ('hidden_params_ids', models.TextField(default='[]', verbose_name='Список идентификаторов скрытых параметров')),
                ('shown_stream_ids', models.TextField(default='[]', verbose_name='Список идентификаторов отображаемых видеопотоков')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Настройки',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]
