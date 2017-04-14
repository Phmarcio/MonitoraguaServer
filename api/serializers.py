from rest_framework import serializers
from gerenciar_abastecimento.models import Setor, Bairro, Historico


class SetorSerializer(serializers.HyperlinkedModelSerializer):
    historicos = serializers.HyperlinkedRelatedField(
        view_name='api:historico-detail',
        read_only=True,
        many=True,
    )

    class Meta:
        model = Setor
        fields = ('id', 'nome', 'historicos',)


class HistoricoSerializer(serializers.HyperlinkedModelSerializer):
    setor = serializers.HyperlinkedRelatedField(
        view_name='api:setor-detail',
        read_only=True,
    )

    class Meta:
        model = Historico
        fields = ('id', 'data_inicio', 'data_fim', 'qts_abastecimentos', 'setor',)
