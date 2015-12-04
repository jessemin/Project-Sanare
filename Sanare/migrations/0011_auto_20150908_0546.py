# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanare', '0010_auto_20150908_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchedpair',
            name='name1',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AddField(
            model_name='matchedpair',
            name='name2',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]
