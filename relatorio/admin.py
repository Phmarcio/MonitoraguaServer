# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Relatorio

# Register your models here.

class RelatorioAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'assunto', 'resolvido', 'data_adicao')
    list_filter = ['data_adicao', 'resolvido', 'assunto',]
    search_fields = ('mensagem',)

admin.site.register(Relatorio, RelatorioAdmin)