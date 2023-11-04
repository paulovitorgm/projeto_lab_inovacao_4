from django.contrib import admin
from jogos.models import Jogos, Plataforma


class JogosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'empresa_desenvolvedora', 'ano_lancamento', 'plataforma']
    list_display_links = ['nome', 'empresa_desenvolvedora', 'ano_lancamento', 'plataforma']
    list_filter = ['ano_lancamento']
    list_per_page = 15


class PlataformaAdmin(admin.ModelAdmin):
    list_display = ['id', 'plataforma']
    list_display_links = ['id', 'plataforma']
    list_filter = ['plataforma']


admin.site.register(Jogos, JogosAdmin)
admin.site.register(Plataforma, PlataformaAdmin)
