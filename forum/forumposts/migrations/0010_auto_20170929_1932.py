# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-29 23:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forumposts', '0009_auto_20170929_1931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forumpost',
            old_name='post_id',
            new_name='id',
        ),
    ]
