# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoryList',
            fields=[
                ('categoryName', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('categoryDescription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('productImage', models.ImageField(upload_to='static/products/')),
            ],
        ),
        migrations.CreateModel(
            name='productList',
            fields=[
                ('productCode', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('productDescription', models.TextField()),
                ('category', models.ForeignKey(to='collection.categoryList')),
            ],
        ),
        migrations.AddField(
            model_name='gallery',
            name='prodId',
            field=models.ForeignKey(to='collection.productList'),
        ),
    ]
