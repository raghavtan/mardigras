# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category_list',
            fields=[
                ('category_id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('category_name', models.CharField(max_length=60)),
                ('icon_file_name', models.FilePathField(path='/categories/images')),
            ],
        ),
        migrations.CreateModel(
            name='category_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='category_tree',
            fields=[
                ('path_no', models.IntegerField(primary_key=True, serialize=False)),
                ('child_category', models.ForeignKey(related_name='child', to='collection.category_list')),
                ('parent_category', models.ForeignKey(related_name='parent', to='collection.category_list')),
            ],
        ),
        migrations.CreateModel(
            name='product_list',
            fields=[
                ('product_id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('product_seq', models.CharField(max_length=20)),
                ('product_name', models.CharField(max_length=80)),
                ('product_s_desc', models.TextField()),
                ('product_colors', models.CharField(max_length=20)),
                ('product_sizes', models.CharField(max_length=60)),
                ('product_materials', models.CharField(max_length=20)),
                ('product_flavors', models.CharField(max_length=20)),
                ('product_thumbnail_url', models.FilePathField(path='/products/images/th')),
                ('product_image_url', models.FilePathField(path='/products/images')),
                ('product_extra_flag', models.SmallIntegerField()),
                ('product_date_avail_from', models.DateField(auto_now=True)),
                ('product_date_avail_upto', models.CharField(max_length=20)),
                ('product_list_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_discount_id', models.CharField(max_length=10)),
                ('product_tax_id', models.CharField(max_length=20)),
                ('product_price_struct_id', models.CharField(max_length=20)),
                ('brand_id', models.CharField(max_length=20)),
                ('thumb_ok', models.BooleanField()),
                ('fullpic_ok', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='prodId',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='category',
        ),
        migrations.DeleteModel(
            name='categoryList',
        ),
        migrations.DeleteModel(
            name='gallery',
        ),
        migrations.DeleteModel(
            name='productList',
        ),
        migrations.AddField(
            model_name='category_table',
            name='category_id',
            field=models.ForeignKey(to='collection.product_list'),
        ),
        migrations.AddField(
            model_name='category_table',
            name='product_id',
            field=models.ForeignKey(to='collection.category_list'),
        ),
    ]
