# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-06 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semesterpage', '0019_auto_20170806_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='full_name',
            field=models.CharField(help_text='F.eks. "Prosedyre- og Objektorientert Programmering"', max_length=120, verbose_name='fullt navn'),
        ),
        migrations.AlterField(
            model_name='resourcelinklist',
            name='full_name',
            field=models.CharField(help_text='F.eks. "Prosedyre- og Objektorientert Programmering"', max_length=120, verbose_name='fullt navn'),
        ),
    ]
