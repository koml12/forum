# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-04 15:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forumposts', '0014_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forumpost',
            old_name='id',
            new_name='post_id',
        ),
    ]
