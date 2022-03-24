from django.contrib import admin

from .models import Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'unidade_medida',
                    'quantidade', 'preco')


admin.site.register(Produto, ProdutoAdmin)
