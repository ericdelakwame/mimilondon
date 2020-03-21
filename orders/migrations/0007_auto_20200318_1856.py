# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-03-18 18:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200318_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='options',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='shop.Options'),
        ),
    ]
