# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('address_type', models.CharField(max_length=120, default='Billing address', choices=[('billing', 'Billing address')])),
                ('address_line_1', models.CharField(max_length=120)),
                ('address_line_2', models.CharField(max_length=120, blank=True, null=True)),
                ('city', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120, default='United States of America')),
                ('state', models.CharField(max_length=120)),
                ('postal_code', models.CharField(max_length=120)),
                ('billing_profile', models.ForeignKey(to='billing.BillingProfile')),
            ],
        ),
    ]
