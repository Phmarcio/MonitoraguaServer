# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chamado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(choices=[('OUTROS', 'Outros'), ('CANO QUEBRADO', 'Cano quebrado'), ('IRREGULARIDADE', 'Irregularidade')], default='OUTROS', max_length=128, verbose_name='assunto')),
                ('mensagem', models.TextField(max_length=512)),
                ('endereco', models.TextField(max_length=512)),
                ('data_criacao', models.DateTimeField(auto_now=True, verbose_name='data de criacao')),
            ],
            options={
                'ordering': ('data_criacao',),
                'verbose_name': 'relatorio',
                'verbose_name_plural': 'relatorios',
            },
        ),
    ]
