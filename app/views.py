from django.shortcuts import render
from .models import Produto
from django.shortcuts import get_list_or_404
from django.http import HttpResponse # Cria uma reposta HTTP
from django.template import loader

# Função index passando request como parâmetro
def index(request):
     # variavel produto recebe todos os valores dos objetos de Produto
     produtos = Produto.objects.all()

     # verifica se o usuário que está acessando a página está logado ou não no sistema
     if str(request.user) == 'AnonymousUser':
        login = 'Usuário não registrado'

     else:
        login = 'Usuário logado'

    # Dicionário passando as chaves e valores de elementos especificos, incluindo o próprio teste do dicionário
     context = {
        'teste': 'teste de dicionário funcionando',
        'login': login,
        'produtos': produtos,
    }
     """

      * Retorna a renderização do request da pagina 'index.html', 
      * também napágina é passado o dicionário context, 
      * mostrando todos os seus valores
     
     """
     return render(request, 'index.html', context)

   

def pagina_secundaria(request):
    return render(request, 'pagina_secundaria.html')

def produto(request,pk):
    print(f'PK: {pk}')
    prod = Produto.objects.get(id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

# Função error404, obrigatório ter uma excepction, vulgo, exceções para tratamentos de erros
def error404(request, ex):
    # variável template recebe o carregamento da página 404.html
    template = loader.get_template('404.html')
    """
     * return em Http content recebendo a renderização do template, 
     * tipo do contéudo em HTML, UTF-8 e recebendo o status  de 404
    
    """ 
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
