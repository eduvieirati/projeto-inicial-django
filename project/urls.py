from django.contrib import admin
from django.urls import path, include

""" 

 * Nunca é bom deixar todas as suas rotas dentro de um só arquivo
 * Aqui é bom fazer uma path que inclua todas as suas urls, para evitar invasão no sistema 
 * e localização da pasta raiz

"""
urlpatterns = [
    path('painel_admin/', admin.site.urls),
    path('', include('app.urls'))
]
