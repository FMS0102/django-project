from django import http
from django.shortcuts import render

from app.forms import ProdutoForm
from .models import Produto


def index(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)

        if form.is_valid():
            form.save()
            # HttpResponseRedirect('/') -> redirecionando para uma atualização de página ('/'), para prevenir erros de duplicação de dados.
            return http.HttpResponseRedirect('/')

    form = ProdutoForm()

    produtos = Produto.objects.all()

    context = {
        'produtos': produtos,
        'form': form
    }
    return render(request, 'index.html', context)
