# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciar_abastecimento', '0003_auto_20170414_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico',
            name='data_fim',
            field=models.DateField(blank=True, null=True, verbose_name='data de fim'),
        ),
    ]
