# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Chamado


# Register your models here.

class ChamdoAdmin(admin.ModelAdmin):
    list_display = ('data_criacao', '__str__', 'assunto', 'endereco')
    list_filter = ['data_criacao', 'assunto', ]
    search_fields = ('mensagem', 'endereco',)


admin.site.register(Chamado, ChamdoAdmin)
