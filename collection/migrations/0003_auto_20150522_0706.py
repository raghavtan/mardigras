# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_auto_20150522_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category_list',
            name='icon_file_name',
            field=models.FilePathField(path='/categories/images', blank=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='brand_id',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_colors',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_date_avail_upto',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_discount_id',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_extra_flag',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_flavors',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_image_url',
            field=models.FilePathField(path='/products/images', blank=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_list_price',
            field=models.DecimalField(max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_materials',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_name',
            field=models.CharField(max_length=80, blank=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_price_struct_id',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_s_desc',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_seq',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_sizes',
            field=models.CharField(max_length=60, blank=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_tax_id',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_thumbnail_url',
            field=models.FilePathField(path='/products/images/th', blank=True),
        ),
    ]
