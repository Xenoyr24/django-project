# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=225)),
                ('slug', models.SlugField(unique=True, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True, blank=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(default=100, max_digits=20, decimal_places=2)),
                ('image', models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_path)),
                ('featured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ForeignKey(blank=True, related_name='Category', to='products.Category')),
            ],
        ),
    ]
