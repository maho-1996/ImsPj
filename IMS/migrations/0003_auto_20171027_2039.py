# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-27 12:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0002_auto_20171027_2037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['id']},
        ),
    ]
