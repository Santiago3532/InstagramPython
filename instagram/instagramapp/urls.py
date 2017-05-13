from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$', views.registrar, name = 'registrar'),
    url(r'^inicio/$', views.iniciar, name = 'iniciar'),
    url(r'^home/$', views.home, name = 'home')
]
