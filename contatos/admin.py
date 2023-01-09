from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'telefone', 'email', 'categoria') #Informações disponíveis
    list_display_links = ('nome', 'sobrenome') #Link para edição do contato nas categorias 
    list_filter = ('nome', 'sobrenome') #Filtros por categoria
    list_per_page = 10 #Contatos por página
    search_fields = ('nome', 'sobrenome', 'telefone') #Campo de pesquisa


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)