# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciar_abastecimento', '0004_auto_20170414_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico',
            name='setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='setor', to='gerenciar_abastecimento.Setor'),
        ),
    ]