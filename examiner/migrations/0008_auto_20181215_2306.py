# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-15 22:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examiner', '0007_auto_20181215_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapedpdf',
            name='sha1_hash',
            field=models.CharField(help_text='Unik sha1 hash relativt til filinnhold.', max_length=40, unique=True, validators=[django.core.validators.RegexValidator(message='Not a valid SHA1 hash string.', regex='^[0-9a-f]{40}$')]),
        ),
    ]
