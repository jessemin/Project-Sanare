# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Sanare', '0008_auto_20150908_0239'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchedPair',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id1', models.CharField(max_length=30)),
                ('id2', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'published')),
            ],
        ),
    ]
