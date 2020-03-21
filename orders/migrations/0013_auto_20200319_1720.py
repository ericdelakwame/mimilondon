# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-03-19 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20200319_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='options',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='shop.Options'),
        ),
    ]