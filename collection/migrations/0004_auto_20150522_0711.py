# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_auto_20150522_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category_list',
            name='icon_file_name',
            field=models.FilePathField(blank=True, path='/categories/images', null=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='brand_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='fullpic_ok',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_colors',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_date_avail_from',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_date_avail_upto',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_discount_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_extra_flag',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_flavors',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_image_url',
            field=models.FilePathField(blank=True, path='/products/images', null=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_list_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_materials',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_price_struct_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_s_desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_seq',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_sizes',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_tax_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_thumbnail_url',
            field=models.FilePathField(blank=True, path='/products/images/th', null=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='thumb_ok',
            field=models.NullBooleanField(),
        ),
    ]
