# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0002_curso_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('abrev', models.CharField(blank=True, null=True, max_length=10)),
                ('desc', models.TextField(max_length=60)),
            ],
            options={
                'verbose_name_plural': 'Ciclos',
                'verbose_name': 'Ciclo',
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='ciclo',
            field=models.ForeignKey(null=True, to='carga.Ciclo', blank=True),
        ),
    ]
