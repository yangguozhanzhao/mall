# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-26 01:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20171025_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='goods_amount',
        ),
    ]
