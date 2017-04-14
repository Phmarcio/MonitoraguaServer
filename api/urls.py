from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'api'

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^setores/$', views.SetorList.as_view(), name='setor-list'),
    url(r'^setores/(?P<pk>[0-9]+)/$', views.SetorDetail.as_view(), name='setor-detail'),

    url(r'^bairros/$', views.BairroList.as_view(), name='bairro-list'),
    url(r'^bairros/(?P<pk>[0-9]+)/$', views.BairroDetail.as_view(), name='bairro-detail'),
    url(r'^bairros/notificar/(?P<pk>[0-9]+)/$', views.NotificarAbastecimento.as_view(), name='notificar'),

    url(r'^historicos/$', views.HistoricoList.as_view(), name='historico-list'),
    url(r'^historicos/(?P<pk>[0-9]+)/$', views.HistoricoDetail.as_view(), name='historico-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
