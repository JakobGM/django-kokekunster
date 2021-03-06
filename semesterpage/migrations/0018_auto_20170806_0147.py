# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-05 23:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('semesterpage', '0017_auto_20170805_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Hvem som opprettet faget.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_courses', to='semesterpage.Contributor'),
        ),
        migrations.AlterField(
            model_name='options',
            name='active_dataporten_courses',
            field=models.ManyToManyField(blank=True, default=None, help_text='Aktive fag fra dataporten', related_name='active_students', to='semesterpage.Course', verbose_name='dataporten fag'),
        ),
    ]
