# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-15 13:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import semesterpage.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('semesterpage', '0023_auto_20170809_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=semesterpage.models.course_file_path)),
                ('display_name', models.CharField(blank=True, help_text='F.eks. "Kompendium"', max_length=60, verbose_name='visningsnavn')),
                ('order', models.PositiveSmallIntegerField(default=0, help_text='Bestemmer hvilken rekkefølge filene skal vises i. Lavest kommer først.', verbose_name='rekkefølge')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_uploads', to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploads', to='semesterpage.Course')),
            ],
            options={
                'verbose_name': 'fil',
                'verbose_name_plural': 'filer',
                'ordering': ('order',),
            },
        ),
    ]
