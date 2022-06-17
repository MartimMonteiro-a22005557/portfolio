#  hello/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.urls import path

from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('sobremim', views.sobremim_page_view, name='sobremim'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('web', views.web_page_view, name='web'),

    path('blog', views.blog_page_view, name='blog'),
    path('contacto', views.contacto_page_view, name='contacto'),
    path('newpost', views.newpost_page_view, name='newpost'),
    path('quiz', views.quiz_page_view, name='quiz'),
    path('login', views.login_page_view, name='login'),
    path('logout', views.logout_page_view, name='logout'),
    path('editar', views.editar_page_view, name='editar'),
    path('lista', views.lista_page_view, name='lista'),
    path('criar', views.criar_page_view, name='criar')

]
