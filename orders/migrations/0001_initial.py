# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
        ('addresses', '0001_initial'),
        ('products', '__first__'),
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('order_id', models.CharField(max_length=120, blank=True)),
                ('billing_address_final', models.TextField(blank=True, null=True)),
                ('status', models.CharField(max_length=120, default='created', choices=[('created', 'Created'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('refunded', 'Refunded')])),
                ('shipping_total', models.DecimalField(default=5.99, max_digits=65, decimal_places=2)),
                ('total', models.DecimalField(default=0.0, max_digits=65, decimal_places=2)),
                ('active', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('billing_address', models.ForeignKey(blank=True, null=True, related_name='billing_address', to='addresses.Address')),
                ('billing_profile', models.ForeignKey(blank=True, null=True, to='billing.BillingProfile')),
                ('cart', models.ForeignKey(to='carts.Cart')),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='ProductPurchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('order_id', models.CharField(max_length=120)),
                ('refunded', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('billing_profile', models.ForeignKey(to='billing.BillingProfile')),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
    ]
