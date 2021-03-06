# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ward_ID', models.CharField(max_length=55, verbose_name='Ward_ID')),
                ('Patient_ID', models.CharField(max_length=55, verbose_name='Patient_ID')),
                ('Status', models.CharField(blank=True, max_length=10, null=True, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'WARD',
                'verbose_name_plural': 'WARDS',
            },
        ),
    ]
