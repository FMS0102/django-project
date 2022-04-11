from django import forms
from .models import *


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["descricao", "unidade_medida",
                  "quantidade", "preco", "data_entrada"]
        # método utilizado para esconder o campo 'data_entrada' no formulário e manter o registro no banco de dados,
        # considerando somente o valor padrão definido no 'models.py'
        widgets = {'data_entrada': forms.HiddenInput()}
