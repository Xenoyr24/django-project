# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('email', models.EmailField(max_length=254)),
                ('active', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('other_name', models.CharField(max_length=100, blank=True, default='')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('district', models.CharField(max_length=120, default='Port Louis', choices=[('Port Louis', 'Port-Louis'), ('Flacq', 'Flacq'), ('Grand Port', 'Grand Port'), ('Moka', 'Moka'), ('Plaines Wilhems', 'Plaines Wilhems'), ('Riviere du Rempart', 'Riviere du Rempart'), ('Riviere Noire', 'Riviere Noire'), ('Savanne', 'Savanne'), ('Pamplemousses', 'Pamplemousses')])),
                ('bio', models.TextField(max_length=500, blank=True)),
                ('phone', models.IntegerField(blank=True, default=0)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
