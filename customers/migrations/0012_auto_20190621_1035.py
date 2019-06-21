# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-21 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0011_auto_20190619_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Litres',
            field=models.CharField(choices=[('40Ltrs', '40Ltrs'), ('60Ltrs', '60Ltrs'), ('80Ltrs', '80Ltrs'), ('100Ltrs', '100Ltrs'), ('120Ltrs', '120Ltrs'), ('140Ltrs', '140Ltrs'), ('160Ltrs', '160Ltrs'), ('180Ltrs', '180Ltrs'), ('200Ltrs', '200Ltrs'), ('300Ltrs', '300Ltrs'), ('1000Ltrs', '1000Ltrs'), ('2000Ltrs', '2000Ltrs'), ('3000Ltrs', '3000Ltrs'), ('4000Ltrs', '4000Ltrs'), ('5000Ltrs', '5000Ltrs'), ('10000Ltrs', '1000Ltrs')], default='40Ltrs', max_length=120),
        ),
    ]