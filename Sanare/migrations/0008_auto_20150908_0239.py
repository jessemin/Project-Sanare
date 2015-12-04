# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Sanare', '0007_auto_20150908_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lovepost',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'published'),
        ),
    ]
