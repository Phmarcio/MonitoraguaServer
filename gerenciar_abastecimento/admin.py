# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Historico, Setor, Bairro

# Register your models here.

class HistoricoInLine(admin.StackedInline):
    model = Historico
    extra = 0
    classes = ['collapse']


class SetorAdmin(admin.ModelAdmin):
    list_display =  ('nome', 'em_abastecimento')
    inlines = [HistoricoInLine]


class BairroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'em_abastecimento')
    list_filter = ['setor']
    search_fields = ['nome']



admin.site.register(Setor, SetorAdmin)
admin.site.register(Bairro, BairroAdmin)