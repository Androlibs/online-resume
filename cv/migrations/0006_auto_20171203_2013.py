# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_auto_20171203_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='institute_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='education',
            name='subject',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='interest',
            field=models.CharField(blank=True, help_text='Sparate interests by comma', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='nationality',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='skills',
            field=models.CharField(blank=True, help_text='Sparate Skills by comma', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='job_title',
            field=models.CharField(max_length=100),
        ),
    ]
