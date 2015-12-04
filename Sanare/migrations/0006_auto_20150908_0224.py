# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanare', '0005_auto_20150908_0221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lovepost',
            old_name='receive_id',
            new_name='receiver_id',
        ),
    ]
