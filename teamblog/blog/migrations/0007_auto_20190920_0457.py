# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-09-20 04:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_information_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
    ]