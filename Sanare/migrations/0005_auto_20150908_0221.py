# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanare', '0004_auto_20150908_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lovepost',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name=b'date published'),
        ),
    ]
