# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-03-18 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20200318_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='color',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]