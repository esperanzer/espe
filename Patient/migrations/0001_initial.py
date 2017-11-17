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
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_ID', models.CharField(blank=True, max_length=55, null=True, verbose_name='Patient_ID')),
                ('Patient_Name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Patient_Name')),
                ('Gender', models.CharField(max_length=1, verbose_name='Gender(F or M)')),
                ('Home_Address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Home_Address')),
                ('Date_Of_Birth', models.DateField(verbose_name='Date_Of_Birth')),
                ('Doctor_ID', models.CharField(max_length=55, verbose_name='Doctor_ID')),
                ('Contact', models.CharField(max_length=55, verbose_name='Contact')),
                ('Email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'PATIENT',
                'verbose_name_plural': 'PATIENTS',
            },
        ),
    ]
