# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-29 22:08
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('forumposts', '0006_auto_20170929_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='post_id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique id for this post', primary_key=True, serialize=False),
        ),
    ]
