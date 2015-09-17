# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0005_auto_20150909_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ciclo',
            old_name='desc',
            new_name='descr',
        ),
    ]
