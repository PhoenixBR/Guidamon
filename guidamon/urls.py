from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$','views.site.index', name='pagina_index'),
    url(r'^adocao/$','views.site.adocao', name='pagina_de_adocao'),
    url(r'^adotar/(\d+)/$','views.site.adotar'),
    url(r'^lista_guidus','views.site.lista_guidus', name='pagina_da_lista'),
    url(r'^login/$',"django.contrib.auth.views.login", 
        {"template_name": "pagina_inicial.html"}),
    url(r'^logout/', "django.contrib.auth.views.logout_then_login", 
                                {"login_url": '/login/'}),
    url(r'^cadastrar/$', 'views.site.cadastrar', name='pagina_de_cadastro'),

    
    url(r'^(\d+)/alimentar/(\d+)/$','views.site.alimentar'),
    url(r'^(\d+)/banheiro/(\d+)/$','views.site.banheiro'),
    url(r'^(\d+)/banhar/(\d+)/$','views.site.banhar'),
    url(r'^(\d+)/divertir/(\d+)/$','views.site.divertir'),
    url(r'^(\d+)/socializar/(\d+)/$','views.site.socializar'),
    url(r'^(\d+)/dormir/$','views.site.dormir'),
    url(r'^(\d+)/acordar/$','views.site.acordar'),
    url(r'^(\d+)/enterrar_guidu/$','views.site.enterrar_guidu'),
    
    url(r'^loja/$','views.site.loja', name='pagina_da_loja'),
    url(r'^comprar_livro/(\d+)/$','views.site.comprar_livro'),

    url(r'^itens/$','views.site.itens_comprados', name='pagina_itens_comprados'),
    url(r'^(\d+)/treinar_guidu/$','views.site.treinar_guidu_escolher_golpe'),
    url(r'^(\d+)/treinar_guidu/(\d+)/$','views.site.treinar_guidu'),
    url(r'^(\d+)/pausar_treino/$','views.site.pausar_treino'),
    url(r'^(\d+)/treinar_outro_golpe/(\d+)/$','views.site.treinar_outro_golpe'),

    url(r'^(\d+)/lutar/$','views.site.pagina_lutas'),
    url(r'^(\d+)/lutar/(\d+)/$','views.site.pagina_lutas'),   
    


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
)


if settings.DEBUG:
    urlpatterns += patterns('', (r'^arquivos/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),)

