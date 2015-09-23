# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mardi', '0003_menulist_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='menulist',
            name='urlField',
            field=models.CharField(default=datetime.datetime(2015, 5, 20, 22, 1, 41, 769229, tzinfo=utc), max_length=40),
            preserve_default=False,
        ),
    ]
