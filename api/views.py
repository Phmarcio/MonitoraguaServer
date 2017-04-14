# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from .serializers import SetorSerializer, HistoricoSerializer
from gerenciar_abastecimento.models import Setor, Historico
# Create your views here.

class Setores(APIView):
    """
    Recupera todos os setores
    """

    def get(self, request, format=None):
        serializer_context = {
            'request': request
        }
        setores = Setor.objects.all()
        serializer = SetorSerializer(setores, context=serializer_context, many=True)
        return Response(serializer.data)


class Historicos(APIView):
    """
    Recupera todo o historico
    """

    def get(self, request, format=None):
        serializer_context = {
            'request': request
        }
        historicos = Historico.objects.all()
        serializer = HistoricoSerializer(historicos, context=serializer_context, many=True)
        return Response(serializer.data)