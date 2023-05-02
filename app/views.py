from django.shortcuts import render
from .models import Produto

def index(request):
     produtos = Produto.objects.all()
     if str(request.user) == 'AnonymousUser':
        login = 'Usuário não registrado'

     else:
        login = 'Usuário logado'

     context = {
        'teste': 'teste de dicionário funcionando',
        'login': login,
        'produtos': produtos,
    }
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
