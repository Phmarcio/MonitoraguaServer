# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

OUTROS = 'OUTROS'
CANO_QUEBRADO = 'CANO QUEBRADO'
IRREGULARIDADE = 'IRREGULARIDADE'
TIPO_ASSUNTO = (
    (OUTROS, 'Outros'),
    (CANO_QUEBRADO, 'Cano quebrado'),
    (IRREGULARIDADE, 'Irregularidade'),
)


@python_2_unicode_compatible
class Chamado(models.Model):
    assunto = models.CharField('assunto', max_length=128, choices=TIPO_ASSUNTO, default=OUTROS)
    mensagem = models.TextField(max_length=512,
                                blank=False, null=False)
    endereco = models.TextField(max_length=512,
                                blank=False, null=False)
    data_criacao = models.DateTimeField('data de criacao', auto_now=True)

    def __str__(self):
        '''
        Retorna no máxomp 30 caracteres da mensagem, caso tenha mais ele retorna adicionando '...'
        :return: mensagem
        '''
        return '%s' % (self.mensagem[:30] if len(self.mensagem) <= 30 else self.mensagem[:30] + '...')

    class Meta:
        verbose_name = 'relatorio'
        verbose_name_plural = 'relatorios'
        ordering = ('data_criacao',)
