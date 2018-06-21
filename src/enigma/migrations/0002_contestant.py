# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-21 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enigma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contestant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_finished', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
