# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0008_auto_20150917_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciclo',
            name='descr',
            field=models.CharField(max_length=60),
        ),
    ]
