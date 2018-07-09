# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('Jan', 'January'), ('Feb', 'February'), ('Mar', 'March'), ('Apr', 'April'), ('May', 'May'), ('Jun', 'June'), ('Jul', 'July'), ('Aug', 'August'), ('Sept', 'September'), ('Oct', 'October'), ('Nov', 'November'), ('Dec', 'December')], max_length=4, verbose_name='Month')),
                ('day', models.IntegerField(verbose_name='Day')),
                ('time', models.CharField(choices=[('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('1:00', '1:00'), ('1:30', '1:30'), ('2:00', '2:00'), ('2:30', '2:30'), ('3:00', '3:00'), ('3:30', '3:30'), ('4:00', '4:00'), ('4:30', '4:30'), ('5:00', '5:00'), ('5:30', '5:30'), ('6:00', '6:00'), ('6:30', '6:30'), ('7:00', '7:00'), ('7:30', '7:30'), ('8:00', '8:00')], max_length=5, verbose_name='Game Time')),
                ('away_team', models.CharField(max_length=30, verbose_name='Away Team')),
                ('home_team', models.CharField(max_length=30, verbose_name='Home Team')),
                ('away_team_score', models.IntegerField(verbose_name='Away Team Score')),
                ('home_team_score', models.IntegerField(verbose_name='Home Team Score')),
            ],
        ),
    ]
