# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


def mudar_status_setor(pk):
    setores = Setor.objects.all()

    for setor in setores:
        if setor.id != pk:
            print "setor com o status para false: " + setor.nome

            setor.em_abastecimento = False
            historico_atual = setor.historicos.get_queryset().last()
            historico_atual.data_fim = timezone.now()
            historico_atual.save()

            bairros = setor.bairros.get_queryset()
            for bairro in bairros:
                bairro.em_abastecimento = False
                bairro.save()

            setor.save()


# Create your models here.
@python_2_unicode_compatible
class Setor(models.Model):
    nome = models.CharField("nome", max_length=128, blank=False, null=False)
    em_abastecimento = models.BooleanField("Em abastecimento?", default=False)

    class Meta:
        verbose_name = 'setor'
        verbose_name_plural = 'setores'
        ordering = ('nome',)

    def __str__(self):
        return self.nome

    def noticar_abastecimento(self):
        historico_atual = self.historicos.get_queryset().last()

        if historico_atual:
            if historico_atual.data_fim:
                # Se o último historico já tiver data de fim ele cria um novo
                if (timezone.now() - datetime.timedelta(days=3)).date() > historico_atual.data_fim:
                    # se não existir ele cria um novo e muda o status dos demais setores
                    historico_atual = self.historicos.create()
                else:
                    return "Este setor foi abastecido no dia %s ao dia %s" % (
                        historico_atual.data_inicio.strftime("%d/%m/%Y"),
                        historico_atual.data_fim.strftime("%d/%m/%Y"))
        else:
            # se não existir ele cria um novo e muda o status dos demais setores
            historico_atual = self.historicos.create()

        historico_atual.qts_abastecimentos += 1
        historico_atual.save()
        if historico_atual.qts_abastecimentos >= 5:
            self.em_abastecimento = True
            #  muda o estados de de abastecimento para falso e altera o status de cada bairro
            mudar_status_setor(self.id)
        self.save()

        return "Obrigado por notificar!"


@python_2_unicode_compatible
class Bairro(models.Model):
    nome = models.CharField("nome", max_length=128, blank=False, null=False)
    em_abastecimento = models.BooleanField("Em abastecimento?", default=False)
    setor = models.ForeignKey(Setor, related_name='bairros', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'bairro'
        verbose_name_plural = 'bairros'
        ordering = ('nome',)

    def __str__(self):
        return self.nome

    def get_abastecido(self):
        resposta = self.setor.noticar_abastecimento()

        if not (self.em_abastecimento):
            if self.setor.em_abastecimento:
                self.em_abastecimento = True
                self.save()

        return resposta


@python_2_unicode_compatible
class Historico(models.Model):
    data_inicio = models.DateField("data de início", default=timezone.now)
    data_fim = models.DateField("data de fim", null=True, blank=True)
    qts_abastecimentos = models.PositiveIntegerField('residências com água', default=0)
    setor = models.ForeignKey(Setor, related_name='historicos', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'histórico'
        verbose_name_plural = 'históricos'
        ordering = ('data_inicio', 'data_fim',)

    def __str__(self):
        return "Data de início: %s - Data de fim: %s" % (self.data_inicio, self.data_fim)
