# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0003_curso_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('abrev', models.CharField(blank=True, null=True, max_length=10)),
                ('descr', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Ciclo',
                'verbose_name_plural': 'Ciclos',
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='ciclo',
            field=models.ForeignKey(blank=True, null=True, to='carga.Ciclo'),
        ),
    ]
