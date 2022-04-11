from concurrent.futures.process import _threads_wakeups
from datetime import datetime
from django.db import models

# drop menu com lista de opções cadastradas para preenchimento no formulário
DROP_MENU = [
    ('Metros', 'MT'),
    ('Unidade', 'UN'),
    ('Metro Cubico', 'M3'),
    ('Metro Quadrado', 'M2'),
    ('Quilo', 'KG'),
    ('Tonelada', 'TO'),
    ('Conjunto', 'CJ'),
    ('Peça', 'PC'),
    ('Pacote', 'PT'),
]


class Produto(models.Model):
    descricao = models.CharField('Descrição', max_length=200)
    # no campo 'unidade_medida' foi considerado os valores da lista 'DROP_MENU' no atributo choices
    unidade_medida = models.CharField(
        'Unidade de Medida', choices=DROP_MENU, max_length=14)
    quantidade = models.DecimalField(
        'Quantidade', decimal_places=2, max_digits=8)
    preco = models.DecimalField('Preço Unitário', decimal_places=2, max_digits=8)
    # DateTimeField -> definido valor padrão de hora atual através da biblioteca 'datetime' para o campo 'data_entrada'
    data_entrada = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.descricao
