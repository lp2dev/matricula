# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0007_auto_20150917_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciclo',
            name='descr',
            field=models.TextField(),
        ),
    ]
