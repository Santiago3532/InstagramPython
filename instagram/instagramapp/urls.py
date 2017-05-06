from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^', views.registrar, name = 'registrar'),
    url(r'^Inicio/', views.iniciar, name = 'iniciar')
]
