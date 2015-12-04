# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Sanare', '0003_auto_20150908_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lovepost',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 2, 19, 34, 569008), verbose_name=b'date published', blank=True),
        ),
    ]
