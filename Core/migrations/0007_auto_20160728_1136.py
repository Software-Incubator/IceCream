# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Core', '0006_member_pic_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='facebook',
            field=models.CharField(default=None, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='github',
            field=models.CharField(default=None, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='linkedin',
            field=models.CharField(default=None, max_length=225, null=True),
        ),
    ]