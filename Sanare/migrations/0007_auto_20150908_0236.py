# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanare', '0006_auto_20150908_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='lovepost',
            name='is_old',
            field=models.BooleanField(default=False, verbose_name=b'outdated'),
        ),
        migrations.AlterField(
            model_name='lovepost',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name=b'published'),
        ),
    ]
