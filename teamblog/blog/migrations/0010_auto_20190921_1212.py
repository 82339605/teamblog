# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-09-21 12:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_topic'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='topic',
            table='topic',
        ),
    ]