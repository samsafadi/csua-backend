# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-05 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_data', '0003_auto_20161105_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politburo',
            name='description',
            field=models.CharField(max_length=355),
        ),
    ]