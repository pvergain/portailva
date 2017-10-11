# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-18 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0011_auto_20161123_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='association',
            name='active_members_number',
            field=models.PositiveIntegerField(default=0, verbose_name='Nombre de membres actifs'),
        ),
    ]
