# Generated by Django 3.1.7 on 2021-03-25 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_e', models.FloatField(default=4016594.740906363, verbose_name='Координата E')),
                ('position_n', models.FloatField(default=6977780.708997443, verbose_name='Координата N')),
                ('zoom', models.FloatField(default=11, verbose_name='Приближение')),
                ('status_bar', models.CharField(default='Орел', max_length=200, verbose_name='Состояние')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Данные',
                'verbose_name_plural': 'Данные',
            },
        ),
    ]