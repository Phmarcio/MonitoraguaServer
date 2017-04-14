from django.conf.urls import url
from . import views

app_name = 'api'

urlpatterns = [
    url(r'^setores/$', views.Setores.as_view(), name='setores'),
    url(r'^historicos/$', views.Historicos.as_view(), name='historicos'),
]