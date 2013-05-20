# importamos o modulo de admin
from django.contrib import admin

from jogador.models import Jogador
from guidu.models import Guidu
from guidu.models import GuiduTipo
from golpe.models import Golpe, Livro


class JogadorAdmin(admin.ModelAdmin):
	#fields especifica quais atributos aparecem no form
	list_display = ('user','guicoin','guimoves')
 
class GuiduAdmin(admin.ModelAdmin):
	list_display = ('jogador', 'nome', 'id')

class GolpeAdmin(admin.ModelAdmin):
	list_display = ('nome','poder','velocidade','nivel','tipo')

class GuiduTipoAdmin(admin.ModelAdmin):
	pass

class LivroAdmin(admin.ModelAdmin):
	list_display=('nome','preco', 'tipo')

admin.site.register(Jogador, JogadorAdmin)
admin.site.register(Guidu, GuiduAdmin)
admin.site.register(GuiduTipo, GuiduTipoAdmin)
admin.site.register(Golpe, GolpeAdmin)
admin.site.register(Livro, LivroAdmin)