from django.urls import path
from .views import index, pagina_secundaria, produto


"""

 * Pattern para urls, 
 * Primeiro parâmetro da função é passado o caminho dentro da url
 * Segundo parâmetro é passado a função dela quer foi criada em app.views
 * Terceiro parâmetro é passado o name que vai ser referênciado na url usando o python

"""
urlpatterns = [
    path('',  index, name='index'),
    path('pagina_secundaria', pagina_secundaria, name='pag_second'),
    path('produto/<int:pk>', produto, name='produto'),
]