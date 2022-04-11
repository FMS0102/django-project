from datetime import datetime
from django import http
from django.shortcuts import render

from .forms import ProdutoForm
from .models import Produto

def index(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            # HttpResponseRedirect('/') -> foi necessário o redirecionamento no final da requisição para uma atualização de página ('/'), 
            # afim de evitar erros de registros duplicados.
            return http.HttpResponseRedirect('/')

    form = ProdutoForm()

    produtos = Produto.objects.all()

    # para chamar o formulário e a tabela com o banco de dados em uma única página,
    # foi necessário a crição de dois atributos no context: 
    # form que contém o formulário da página e produtos que contém os produtos apresentados na tabela.
    context = {
        'produtos': produtos,
        'form': form
    }
    return render(request, 'index.html', context)
