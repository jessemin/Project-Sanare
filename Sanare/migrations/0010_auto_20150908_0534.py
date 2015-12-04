# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanare', '0009_matchedpair'),
    ]

    operations = [
        migrations.AddField(
            model_name='lovepost',
            name='receiver_name',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AddField(
            model_name='lovepost',
            name='sender_name',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]
