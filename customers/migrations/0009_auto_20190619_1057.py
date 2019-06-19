# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-19 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_auto_20190617_0959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Street_address',
            new_name='Street_addres',
        ),
        migrations.AlterField(
            model_name='customer',
            name='Litres',
            field=models.CharField(choices=[('40Ltrs', '40Ltrs'), ('60Ltrs', '60Ltrs'), ('80Ltrs', '80Ltrs'), ('100Ltrs', '100Ltrs'), ('120Ltrs', '120Ltrs'), ('140Ltrs', '140Ltrs'), ('160Ltrs', '160Ltrs'), ('180Ltrs', '180Ltrs'), ('200Ltrs', '200Ltrs')], default='40Ltrs', max_length=120),
        ),
    ]
