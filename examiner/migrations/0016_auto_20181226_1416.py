# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-26 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examiner', '0015_auto_20181225_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='course',
            field=models.ForeignKey(blank=True, help_text='Faget som eksamenen tilhører.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='semesterpage.Course'),
        ),
    ]
