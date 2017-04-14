# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializers import SetorSerializer, HistoricoSerializer, BairroSerializer
from gerenciar_abastecimento.models import Setor, Historico, Bairro


# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'setores': reverse('api:setor-list', request=request, format=format),
        'bairros': reverse('api:bairro-list', request=request, format=format),
        'historicos': reverse('api:historico-list', request=request, format=format)
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
