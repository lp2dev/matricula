# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0003_auto_20150826_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='NaturalPerson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('last_name', models.CharField(blank=True, max_length=10, null=True)),
                ('first_name', models.TextField(max_length=60)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'NaturalPerson',
                'verbose_name_plural': 'NaturalPersons',
            },
        ),
    ]
