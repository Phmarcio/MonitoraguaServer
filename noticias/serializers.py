# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Noticia


class NoticiaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Noticia
        fields = ('id', 'mensagem', 'data_criacao', 'ativo',)
