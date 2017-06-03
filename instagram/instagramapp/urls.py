from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns=[
    url(r'^$', views.registrar, name = 'registrar'),
    url(r'^inicio/$', views.iniciar, name = 'iniciar'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^crear_usuario/$', views.crear_usuario, name = 'crear_usuario'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name = 'ins.html', redirect_authenticated_user = True),name = "login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name = 'inicio.html'), name = "logout")
]
