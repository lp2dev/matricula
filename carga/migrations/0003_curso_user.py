# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carga', '0002_curso_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
    ]
