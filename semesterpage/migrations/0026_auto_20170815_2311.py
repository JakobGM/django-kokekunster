# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-15 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semesterpage', '0025_auto_20170815_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='display_name',
            field=models.CharField(blank=True, help_text='Dette er teksten som vises under logen til faget i fagoversikten. F.eks. "C++".', max_length=60, verbose_name='visningsnavn'),
        ),
        migrations.AlterField(
            model_name='courselink',
            name='category',
            field=models.CharField(blank=True, choices=[('tasks.svg', 'Øvinger og prosjekter'), ('blackboard.svg', 'Blackboard'), ('solutions.svg', 'Løsningsforslag'), ('videos.svg', 'Videoforelesninger'), ('timetable.svg', 'Framdrifts- og timeplaner'), ('syllabus.svg', 'Pensum'), ('formulas.svg', 'Formelark'), ('exams.svg', 'Eksamener'), ('facebook.svg', 'Facebook'), ('info.svg', 'Informasjon'), ('important_info.svg', 'Viktig informasjon'), ('ntnu.svg', 'NTNU-lenker'), ('wikipendium.svg', 'Wikipendium'), ('book.svg', 'Pensumbok'), ('quiz.svg', 'Quiz og punktlister'), ('software.svg', 'Programvare')], default=None, help_text='F.eks. "Løsningsforslag". Valget bestemmer hvilket "mini-ikon" som plasseres ved siden av lenken.', max_length=60, null=True, verbose_name='Kateogri'),
        ),
        migrations.AlterField(
            model_name='resourcelink',
            name='category',
            field=models.CharField(blank=True, choices=[('tasks.svg', 'Øvinger og prosjekter'), ('blackboard.svg', 'Blackboard'), ('solutions.svg', 'Løsningsforslag'), ('videos.svg', 'Videoforelesninger'), ('timetable.svg', 'Framdrifts- og timeplaner'), ('syllabus.svg', 'Pensum'), ('formulas.svg', 'Formelark'), ('exams.svg', 'Eksamener'), ('facebook.svg', 'Facebook'), ('info.svg', 'Informasjon'), ('important_info.svg', 'Viktig informasjon'), ('ntnu.svg', 'NTNU-lenker'), ('wikipendium.svg', 'Wikipendium'), ('book.svg', 'Pensumbok'), ('quiz.svg', 'Quiz og punktlister'), ('software.svg', 'Programvare')], default=None, help_text='F.eks. "Løsningsforslag". Valget bestemmer hvilket "mini-ikon" som plasseres ved siden av lenken.', max_length=60, null=True, verbose_name='Kateogri'),
        ),
        migrations.AlterField(
            model_name='resourcelinklist',
            name='display_name',
            field=models.CharField(blank=True, help_text='Dette er teksten som vises under logen til faget i fagoversikten. F.eks. "C++".', max_length=60, verbose_name='visningsnavn'),
        ),
    ]
