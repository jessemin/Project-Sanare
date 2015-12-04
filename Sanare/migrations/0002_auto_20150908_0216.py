# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LovePost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender_id', models.CharField(max_length=30)),
                ('receive_id', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
