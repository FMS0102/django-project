from django import forms
from .models import *


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["descricao", "unidade_medida", "quantidade", "preco"]
