# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-05-31 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20200531_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]