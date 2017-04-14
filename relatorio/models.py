# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

ERRO = 'ERRO'
CRITICA = 'CRITICA'
SUGESTAO = 'SUGESTAO'
TIPO_ASSUNTO = (
    (ERRO, 'Erro'),
    (CRITICA, 'Crítica'),
    (SUGESTAO, 'Sugestão'),
)


@python_2_unicode_compatible
class Relatorio(models.Model):
    assunto = models.CharField('assunto', max_length=128, choices=TIPO_ASSUNTO, default=ERRO)
    mensagem = models.TextField(max_length=512,
                                blank=False, null=False)
    data_adicao = models.DateTimeField('data de adição', auto_now=True)
    resolvido = models.BooleanField('resolvido?', default=False)

    def __str__(self):
        '''
        Retorna no máxomp 30 caracteres da mensagem, caso tenha mais ele retorna adicionando '...'
        :return: mensagem
        '''
        return '%s' % (self.mensagem[:30] if len(self.mensagem) <= 30 else self.mensagem[:30] + '...')

    class Meta:
        verbose_name = 'relatorio'
        verbose_name_plural = 'relatorios'
        ordering = ('data_adicao', 'resolvido',)
