# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2022-09-26 12:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_userprofileinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfile_pic',
            new_name='profile_pic',
        ),
    ]
