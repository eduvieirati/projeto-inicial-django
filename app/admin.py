from django.contrib import admin
from .models import Produto

# Register your models here.

"""

 * Classe produto vai receber uma biblioteca como parâmetro, no caso admin.ModelAdmin
 * e list_display vai para manter a organização na página de cadastrado 
 * e listagem de produtos do adminstrador da aplicação
 *

"""
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

admin.site.register(Produto, ProdutoAdmin)
