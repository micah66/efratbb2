# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0003_auto_20180709_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='away_team_score',
            field=models.IntegerField(blank=True, null=True, verbose_name='Away Team Score'),
        ),
        migrations.AlterField(
            model_name='game',
            name='home_team_score',
            field=models.IntegerField(blank=True, null=True, verbose_name='Home Team Score'),
        ),
    ]
