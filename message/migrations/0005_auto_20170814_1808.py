# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-14 15:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_auto_20170814_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_creation',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 14, 15, 8, 58, 691436, tzinfo=utc)),
        ),
    ]