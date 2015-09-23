# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mardi', '0004_menulist_urlfield'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menulist',
            old_name='urlField',
            new_name='menuUrl',
        ),
    ]
