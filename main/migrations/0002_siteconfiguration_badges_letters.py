# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-22 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_squashed_0003_auto_20190531_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='badges_letters',
            field=models.CharField(default='ce94', max_length=4),
        ),
    ]
