# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-03-15 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid', models.FileField(blank=True, null=True, upload_to='home/vids')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Home Video',
                'verbose_name_plural': 'Home Videos',
            },
        ),
    ]