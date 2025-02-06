from django.conf.urls import url 
from UsuarioApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^tarefa/$',views.tarefaApi),
    url(r'^tarefa/([0-9]+)$',views.tarefaApi),
    
    url(r'^usuario/$',views.usuarioApi),
    url(r'^usuario/([0-9]+)$',views.usuarioApi),
    
    url(r'^SaveFile$', views.SaveFile),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
