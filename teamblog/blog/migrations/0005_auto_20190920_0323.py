# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-09-20 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='time',
            field=models.CharField(max_length=50),
        ),
    ]