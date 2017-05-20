from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$', views.registrar, name = 'registrar'),
    url(r'^inicio/$', views.iniciar, name = 'iniciar'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^crear_usuario/$', views.crear_usuario, name = 'crear_usuario')
]
