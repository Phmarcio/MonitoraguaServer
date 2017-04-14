from rest_framework import serializers
from gerenciar_abastecimento.models import Setor, Bairro, Historico


class SetorSerializer(serializers.HyperlinkedModelSerializer):
    historicos = serializers.HyperlinkedRelatedField(
        view_name='api:historico-detail',
        read_only=True,
        many=True,
    )

    bairros = serializers.HyperlinkedRelatedField(
        view_name='api:bairro-detail',
        read_only=True,
        many=True,
    )

    class Meta:
        model = Setor
        fields = ('id', 'nome', 'em_abastecimento', 'historicos', 'bairros',)


class HistoricoSerializer(serializers.HyperlinkedModelSerializer):
    setor = serializers.HyperlinkedRelatedField(
        view_name='api:setor-detail',
        read_only=True,
    )

    class Meta:
        model = Historico
        fields = ('id', 'data_inicio', 'data_fim', 'qts_abastecimentos', 'setor',)


class BairroSerializer(serializers.HyperlinkedModelSerializer):
    setor = serializers.HyperlinkedRelatedField(
        view_name='api:setor-detail',
        read_only=True,
    )

    notificar = serializers.SerializerMethodField()

    class Meta:
        model = Bairro
        fields = ('id', 'nome', 'em_abastecimento', 'setor', 'notificar')

    def get_notificar(self, obj):
        from rest_framework.reverse import reverse
        request = self.context['request']
        return request.build_absolute_uri(reverse('api:notificar', args=[obj.id]))
