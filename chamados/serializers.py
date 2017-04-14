# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Chamado


class ChamadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chamado
        fields = ('assunto', 'mensagem', 'endereco',)
