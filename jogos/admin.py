from django.contrib import admin
from jogos.models import Jogos


class JogosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'empresa_desenvolvedora', 'ano_lancamento']
    list_display_links = ['nome', 'empresa_desenvolvedora', 'ano_lancamento']
    list_filter = ['ano_lancamento']
    list_per_page = 15


admin.site.register(Jogos, JogosAdmin)
