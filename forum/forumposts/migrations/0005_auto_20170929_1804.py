# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-29 22:04
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('forumposts', '0004_auto_20170511_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumpost',
            name='post_id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique id for this post', unique=True),
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='post_date',
            field=models.DateTimeField(help_text='Date and time that the post was submitted'),
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='post_link',
            field=models.URLField(default='', help_text="Link to the post's content"),
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='post_text',
            field=models.CharField(help_text='Title for the post, typically a description of the URL', max_length=200),
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='votes',
            field=models.IntegerField(default=0, help_text='Number of votes for the post'),
        ),
    ]