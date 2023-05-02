from django.urls import path
from .views import index, pagina_secundaria, produto

urlpatterns = [
    path('',  index, name='index'),
    path('pagina_secundaria', pagina_secundaria, name='pag_second'),
    path('produto/<int:pk>', produto, name='produto'),
]