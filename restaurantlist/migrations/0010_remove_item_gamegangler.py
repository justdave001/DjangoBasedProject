# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-07-07 17:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gamelists1', '0009_item_gamegangler'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='Gamegangler',
        ),
    ]