# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mardi', '0006_auto_20150521_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menulist',
            name='details',
            field=models.TextField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
