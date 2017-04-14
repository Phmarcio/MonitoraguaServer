# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class Noticia(models.Model):
    mensagem = models.TextField('notícia', blank=False)
    data_criacao = models.DateField('data de criação', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        verbose_name = 'notícia'
        verbose_name_plural = 'notícias'
        ordering = ('data_criacao','ativo',)

    def __str__(self):
        '''
       Retorna no máxomp 30 caracteres da mensagem, caso tenha mais ele retorna adicionando '...'
       :return: mensagem
       '''
        return '%s' % (self.mensagem[:30] if len(self.mensagem) <= 30 else self.mensagem[:30] + '...')
