from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext

from guidu.models import GuiduTipo, Guidu
from golpe.models import Livro

def cadastrar(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid(): #podia ser non_fields_error ?
            form.save()
            return redirect(index)
    else:
        form = UserCreationForm()   
    return render_to_response("cadastrar.html", {'form': form}, context_instance=RequestContext(request))

@login_required
def index(request):
    user = request.user
    jogador = user.get_profile()
    guidus = jogador.guidus.all()
    '''jogador.refresh() #nao precisa refrescar o jogador pois toda vez que 
    index.html eh chamado, chama a funcao qnto_falta_acao, que chama jogador.refresh
    lembrar de ter cautela ao alterar essa funcao /\ 
    '''
    #para cada guidu que o jogador tiver, atualiza o guidu, salva no banco e 
    for guidu in guidus:
        guidu.refresh()
        guidu.save()
        jogador = guidu.jogador

    if guidus:
        return render_to_response("index.html", {"guidus": guidus, "jogador": jogador}, context_instance=RequestContext(request))
    else:
        return redirect(adocao)
    
@login_required
def adocao(request):
    profile = request.user.get_profile()
    if profile.guidus.all():    
        return redirect(index)
    guidutipos = GuiduTipo.objects.all()
    return render_to_response("adocao.html",{'guidutipos':guidutipos, "jogador": profile}, context_instance=RequestContext(request))

@login_required
def adotar(request, id_guidutipo):
    profile = request.user.get_profile()
    if profile.guidus.all():
        return redirect(index)
    if request.method == 'POST':
        guidutipo = get_object_or_404(GuiduTipo, pk=id_guidutipo)
        nome = request.POST["botao_cadastrar"]
        guidu = Guidu(nome=nome, jogador=profile, tipo=guidutipo)
        guidu.save()
        return redirect(index)
        
    else:
        return render_to_response("adotar.html", {"jogador": profile}, 
            context_instance=RequestContext(request))

@login_required
def loja(request):
    livros = Livro.objects.all()
    jogador = request.user.get_profile()
    return render_to_response("loja.html", {"livros":livros, "jogador":jogador})

@login_required
def comprar_livro(request, id_livro):
    jogador = request.user.get_profile()
    livro = get_object_or_404(Livro, pk=id_livro)
    #return redirect(index)
    
    if(jogador.guicoin>=livro.preco):
        if(livro not in jogador.livros.all()):
            jogador.livros.add(livro)
            jogador.guicoin -= livro.preco
            jogador.save()
            return render_to_response("livro_comprado.html", {"jogador":jogador}, context_instance=RequestContext(request))
        else:
            return redirect(loja)
    else:
        return render_to_response("livro_ncomprado.html", {"jogador":jogador}, context_instance=RequestContext(request))

@login_required
def itens(request):
    jogador = request.user.get_profile() 
    return render_to_response("itens.html", {"jogador":jogador})

@login_required
def treinar_guidu_escolher_golpe(request, id_golpe):
    jogador = request.user.get_profile()
    return render_to_response("treinar_guidu.html", {"jogador":jogador}, 
                                context_instance=RequestContext(request))

@login_required
def treinar_guidu(request, id_guidu, id_golpe):
    jogador = request.user.get_profile()
    guidu = Guidu.objects.get_object_or_404(pk=id_guidu, jogador=jogador)
    #verificar se já treinou esse golpe
    #verificar se os slots de 5 golpes estão cheios
    #verificar se tem guimoves
    #verificar se já está treinando outro golpe ou mesmo esse 



@login_required
def alimentar(request, id_guidu, id_alimento):
    jogador = request.user.get_profile()
    guidu = get_object_or_404(Guidu, pk=id_guidu, jogador=jogador)
    if jogador.guimoves>0:
        funcionou = guidu.alimentar(id_alimento)
        if funcionou:
            jogador.guimoves -= 1
            jogador.save()
    return redirect(index)

@login_required
def banheiro(request, id_guidu, id_banheiro):
    jogador = request.user.get_profile()
    guidu = get_object_or_404(Guidu, pk=id_guidu, jogador=jogador)
    if jogador.guimoves>0:
        funcionou = guidu.obrar(id_banheiro)
        if funcionou:
            jogador.guimoves -= 1
            jogador.save()
    return redirect(index)

@login_required
def banhar(request, id_guidu, id_banho):
    jogador = request.user.get_profile()
    guidu = get_object_or_404(Guidu, pk=id_guidu, jogador=jogador)
    if jogador.guimoves>0:
        funcionou = guidu.banhar(id_banho)
        if funcionou:
            jogador.guimoves -= 1
            jogador.save()
    return redirect(index)

@login_required
def divertir(request, id_guidu, id_diversao):
    jogador = request.user.get_profile()
    guidu = get_object_or_404(Guidu, pk=id_guidu, jogador=jogador)
    if jogador.guimoves>0:
        funcionou = guidu.divertir(id_diversao)
        if funcionou:
            jogador.guimoves -= 1
            jogador.save()
    return redirect(index)

@login_required
def socializar(request, id_guidu, id_socializar):
    jogador = request.user.get_profile()
    guidu = get_object_or_404(Guidu, pk=id_guidu, jogador=jogador)
    if jogador.guimoves>0:
        funcionou = guidu.socializar(id_socializar)
        if funcionou:
            jogador.guimoves -= 1
            jogador.save()
    return redirect(index)

@login_required
def dormir(request, id_guidu):
    jogador = request.user.get_profile()
    guidu = get_object_or_404(Guidu, pk=id_guidu, jogador=jogador)
    if jogador.guimoves>0:
        funcionou = guidu.dormir()
        if funcionou:
            jogador.guimoves -= 1
            jogador.save()
    return redirect(index)

@login_required
def acordar(request, id_guidu):
    jogador = request.user.get_profile()
    guidu = get_object_or_404(Guidu, pk=id_guidu, jogador=jogador)
    if jogador.guimoves>0:
        funcionou = guidu.acordar()
        if funcionou:
            jogador.guimoves -= 1
            jogador.save()
    return redirect(index)

@login_required
def lista_guidus(request):
    jogador = request.user.get_profile()
    #guidus = Guidu.objects.filter(esta_morto=False).order_by('data_nascimento')
    guidus = Guidu.objects.all().order_by('data_nascimento')
    return render_to_response("lista_guidus.html", {'guidus':guidus, "jogador": jogador})


@login_required
def enterrar_guidu(request, id_guidu):
    jogador = request.user.get_profile()
    guidu = get_object_or_404(Guidu, pk=id_guidu, jogador=jogador)
    print guidu.nome
    guidu.delete()
    return redirect(index)


#verificar se nao eh o caso de colocar jogador.refres antes de todas as acoes.