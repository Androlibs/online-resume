# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20171201_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='tagline',
            field=models.CharField(blank=True, help_text='i.e: Web Developer', max_length=50, null=True),
        ),
    ]
