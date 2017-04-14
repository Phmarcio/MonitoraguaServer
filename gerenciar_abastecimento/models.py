# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Setor(models.Model):
    nome = models.CharField("nome", max_length=128,blank=False, null=False)
    em_abastecimento = models.BooleanField("Em abastecimento?", default=False)

    class Meta:
        verbose_name = 'setor'
        verbose_name_plural = 'setores'
        ordering = ('nome',)

    def __str__(self):
        return self.nome


@python_2_unicode_compatible
class Bairro(models.Model):
    nome = models.CharField("nome", max_length=128, blank=False, null=False)
    em_abastecimento = models.BooleanField("Em abastecimento?", default=False)
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'bairro'
        verbose_name_plural = 'bairros'
        ordering = ('nome',)

    def __str__(self):
        return self.nome



@python_2_unicode_compatible
class Historico(models.Model):
    data_inicio = models.DateField("data de início", default=timezone.now)
    data_fim = models.DateField("data de fim", blank=True)
    qts_abastecimentos = models.PositiveIntegerField('residências com água', default=0)
    setor = models.ForeignKey(Setor,on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'histórico'
        verbose_name_plural = 'históricos'
        ordering = ('data_inicio', 'data_fim',)

    def __str__(self):
        return "Data de início: %s - Data de fim: %s" % (self.data_inicio, self.data_fim)