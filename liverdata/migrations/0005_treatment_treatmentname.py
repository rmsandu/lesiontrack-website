# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('liverdata', '0004_auto_20171018_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='treatmentname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='liverdata.TreatmentName'),
        ),
    ]