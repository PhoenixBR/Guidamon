# importamos o modulo de admin
from django.contrib import admin

from jogador.models import Jogador
from guidu.models import Guidu
from guidu.models import GuiduTipo


class JogadorAdmin(admin.ModelAdmin):
	list_display = ('user','guicoin','guimoves')
 
class GuiduAdmin(admin.ModelAdmin):
	list_display = ('jogador', 'nome')

class GuiduTipoAdmin(admin.ModelAdmin):
	pass

admin.site.register(Jogador, JogadorAdmin)
admin.site.register(Guidu, GuiduAdmin)
admin.site.register(GuiduTipo, GuiduTipoAdmin)