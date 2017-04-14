from rest_framework import serializers
from gerenciar_abastecimento.models import Setor, Bairro, Historico


class SetorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'


class HistoricoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Historico
        fields = '__all__'