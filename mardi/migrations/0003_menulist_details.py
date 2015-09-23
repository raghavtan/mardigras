# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mardi', '0002_auto_20150519_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='menulist',
            name='details',
            field=models.TextField(default=datetime.datetime(2015, 5, 19, 12, 43, 2, 49452, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
