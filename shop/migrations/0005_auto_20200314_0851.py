# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-03-14 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Children', 'Children'), ('Accessories', (('Mens', 'Mens'), ('Womens', 'Womens')))], max_length=50),
        ),
    ]
