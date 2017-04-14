# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Noticia


# Register your models here.

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'data_criacao', 'ativo',)
    list_filter = ['data_criacao', 'ativo', ]
    search_fields = ('mensagem',)


admin.site.register(Noticia, NoticiaAdmin)
