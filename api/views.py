# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

from .serializers import SetorSerializer, HistoricoSerializer, BairroSerializer
from noticias.serializers import NoticiaSerializer
from noticias.models import Noticia

from relatorio.serializers import RelatorioSerializer
from chamados.serializers import ChamadoSerializer
from gerenciar_abastecimento.models import Setor, Historico, Bairro


# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'setores': reverse('api:setor-list', request=request, format=format),
        'bairros': reverse('api:bairro-list', request=request, format=format),
        'historicos': reverse('api:historico-list', request=request, format=format),
        'noticias': reverse('api:noticia-list', request=request, format=format),
        'relatorio': reverse('api:relatorio-assunto-create', request=request, format=format),
        'chamados': reverse('api:chamado-assunto-create', request=request, format=format),
    })


class SetorList(generics.ListCreateAPIView):
    """
    Recupera todos os setores
    """
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer


class SetorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalha um setor
    """
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer


class HistoricoList(generics.ListCreateAPIView):
    """
    Recupera todo o historico
    """
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer


class HistoricoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalha um histórico
    """
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer


class BairroList(generics.ListCreateAPIView):
    """
    Recupera todo o historico
    """
    queryset = Bairro.objects.all()
    serializer_class = BairroSerializer


class BairroDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalha um histórico
    """
    queryset = Bairro.objects.all()
    serializer_class = BairroSerializer


class NotificarAbastecimento(APIView):
    """
    Recupera todos os estados cadastrados no sistema
    """

    def get(self, request, pk, format=None):
        serializer_context = {
            'request': request
        }
        bairro = get_object_or_404(Bairro, pk=pk)
        return Response(bairro.get_abastecido())


class NoticiaList(generics.ListCreateAPIView):
    """
    Recupera todo as notícias
    """
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer


class NoticiaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalha uma notícia
    """
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer


class RelatorioCriar(APIView):
    """
    Relatórios do sistema
    """

    def get(self, request, format=None):
        # capturando a tupla de choices e convertendo para dicionario
        from relatorio.models import TIPO_ASSUNTO
        return Response(dict(map(reversed, TIPO_ASSUNTO)))

    def post(self, request, format=None):
        serializer = RelatorioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChamadoCriar(APIView):
    """
    Chamados no sistema
    """

    def get(self, request, format=None):
        # capturando a tupla de choices e convertendo para dicionario
        from chamados.models import TIPO_ASSUNTO
        return Response(dict(map(reversed, TIPO_ASSUNTO)))

    def post(self, request, format=None):
        serializer = ChamadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
