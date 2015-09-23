# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_auto_20150522_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_list',
            name='category_desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
