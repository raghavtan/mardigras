# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mardi', '0005_auto_20150521_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menulist',
            name='details',
            field=models.TextField(null=True),
        ),
    ]
