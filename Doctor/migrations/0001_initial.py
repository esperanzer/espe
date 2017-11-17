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
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doctor_ID', models.CharField(blank=True, max_length=55, null=True, verbose_name='Doctor ID')),
                ('Doctor_Name', models.CharField(blank=True, max_length=55, null=True, verbose_name='Doctor Name')),
                ('Password', models.CharField(max_length=40, verbose_name='Password')),
                ('Gender', models.CharField(max_length=1, verbose_name='Gender(F or M)')),
                ('Qualification', models.CharField(blank=True, max_length=40, null=True, verbose_name='Qualification')),
                ('Department', models.CharField(blank=True, max_length=55, null=True, verbose_name='Department')),
                ('Contact', models.CharField(blank=True, max_length=40, null=True, verbose_name='Contact')),
                ('Home_Address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Home Address')),
                ('Email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('Appointment_ID', models.CharField(blank=True, max_length=55, null=True, verbose_name='Appointment ID')),
            ],
            options={
                'verbose_name': 'DOCTOR',
                'verbose_name_plural': 'DOCTORS',
            },
        ),
    ]
