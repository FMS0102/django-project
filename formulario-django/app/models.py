from unicodedata import decimal
from django.db import models

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
    unidade_medida = models.CharField(
        'Unidade de Medida', choices=DROP_MENU, max_length=14)
    quantidade = models.DecimalField(
        'Quantidade', decimal_places=2, max_digits=8)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    def __str__(self):
        return self.descricao
