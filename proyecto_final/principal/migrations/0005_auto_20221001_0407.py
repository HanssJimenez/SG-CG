# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2022-10-01 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_inventario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='nombre_p',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
