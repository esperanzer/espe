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
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Treatment_ID', models.CharField(max_length=55, verbose_name='Treatment_ID')),
                ('Patient_Name', models.CharField(blank=True, max_length=55, null=True, verbose_name='Patient_Name')),
                ('Diagnosis', models.CharField(max_length=100, null=True, verbose_name='Diagnosis')),
                ('Patient_ID', models.CharField(max_length=55, verbose_name='Patient_ID')),
                ('Disease', models.CharField(blank=True, max_length=100, null=True, verbose_name='Disease')),
                ('Date_Of_Treatment', models.DateField(verbose_name='Date_Of_Treatmen')),
                ('Details', models.CharField(blank=True, max_length=100, null=True, verbose_name='Details')),
            ],
            options={
                'verbose_name': 'TREATMENT',
                'verbose_name_plural': 'TREATMENTS',
            },
        ),
    ]