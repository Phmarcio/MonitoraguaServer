# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Relatorio


class RelatorioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Relatorio
        fields = ('assunto', 'mensagem',)
