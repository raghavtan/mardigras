# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='menuList',
            fields=[
                ('displayName', models.CharField(serialize=False, primary_key=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='subMenu',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('subName', models.TextField()),
                ('subParent', models.ForeignKey(to='mardi.menuList')),
            ],
        ),
    ]
