# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20160228_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careergoal',
            name='categories',
            field=models.ManyToManyField(blank=True, to='resume.ResumeCategory'),
        ),
        migrations.AlterField(
            model_name='education',
            name='categories',
            field=models.ManyToManyField(blank=True, to='resume.ResumeCategory'),
        ),
        migrations.AlterField(
            model_name='programmingskills',
            name='categories',
            field=models.ManyToManyField(blank=True, to='resume.ResumeCategory'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='categories',
            field=models.ManyToManyField(blank=True, to='resume.ResumeCategory'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='categories',
            field=models.ManyToManyField(blank=True, to='resume.ResumeCategory'),
        ),
    ]
