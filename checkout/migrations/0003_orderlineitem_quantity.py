# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-19 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_remove_orderlineitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]