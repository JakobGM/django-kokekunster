# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-06 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('semesterpage', '0006_auto_20160806_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='homepage',
            field=models.CharField(blank=True, help_text='Fagene du velger nedenfor vil dukke opp på hjemmesiden din. Du kan besøke din personlige semesterside på kokekunster.no/hjemmesidenavn eller hjemmesidenavn.kokekunster.no.', max_length=60, null=True, unique=True, verbose_name='hjemmesidenavn'),
        ),
        migrations.AlterField(
            model_name='options',
            name='self_chosen_courses',
            field=models.ManyToManyField(blank=True, default=None, help_text='Her kan du velge ekstra fag som ikke er en del av semesteret ditt, eller evt. lage en helt egen fagkombinasjon.', related_name='students', to='semesterpage.Course', verbose_name='fag'),
        ),
        migrations.AlterField(
            model_name='options',
            name='self_chosen_semester',
            field=models.ForeignKey(blank=True, default=None, help_text='Alle fagene til dette semesteret vil dukke opp på hjemmesiden din.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='semesterpage.Semester', verbose_name='semester'),
        ),
    ]