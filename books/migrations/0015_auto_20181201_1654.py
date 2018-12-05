# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-01 16:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0014_auto_20181201_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='confirm_your_username',
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
