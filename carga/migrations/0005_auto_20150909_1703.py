# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0004_naturalperson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='ciclo',
            field=models.ForeignKey(to='carga.Ciclo', default=4),
            preserve_default=False,
        ),
    ]
