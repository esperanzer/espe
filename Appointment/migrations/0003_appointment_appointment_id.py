# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0002_auto_20171016_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='Appointment_ID',
            field=models.CharField(blank=True, max_length=55, null=True, verbose_name='Appointment_ID'),
        ),
    ]
