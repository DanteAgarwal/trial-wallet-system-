# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0017_wallet_hmac_or_checksum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='hmac_or_checksum',
            field=models.CharField(blank=True, default='temp_HMAC', max_length=200),
        ),
    ]