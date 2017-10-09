# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-29 23:31
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('forumposts', '0008_auto_20170929_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='post_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
