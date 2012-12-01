from django.shortcuts import HttpResponse, redirect, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext

from guidu.models import GuiduTipo, Guidu
from guidu.form import FormGuidu


def registrar(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid(): #podia ser non_fields_error ?
            form.save()
            redirect(index)
    else:
        form = UserCreationForm()   
    return render_to_response("registrar.html", {'form': form}, context_instance=RequestContext(request))

@login_required
def index(request):
    user = request.user
    jogador = user.get_profile()
    guidus = jogador.guidus.all()
    for guidu in guidus:
        guidu.refresh()

    if guidus:
        return render_to_response("index.html", {"guidus": guidus, "jogador": jogador})
    else:
        return redirect(adocao)
    
@login_required
def adocao(request):
    guidutipos = GuiduTipo.objects.all()
    return render_to_response("adocao.html",{'guidutipos':guidutipos})

@login_required
def adotar(request, id_guidutipo):
    if request.method == 'POST':
        profile = request.user.get_profile()
        guidutipo = get_object_or_404(GuiduTipo, pk=id_guidutipo)
        nome = request.POST["botao_cadastrar"]
        print guidutipo
        guidu = Guidu(nome=nome, jogador=profile, tipo=guidutipo)
        guidu.save()
        return redirect(index)
        
    else:
        form = FormGuidu() 
        return render_to_response("adotar.html", {'form':form}, 
            context_instance=RequestContext(request))

def alimentar(request, id_guidu, id_alimento):
    jogador = request.user.get_profile()
    guidu = get_object_or_404(Guidu, pk=id_guidu, jogador=jogador)
    if jogador.guimoves>0:
        funcionou = guidu.alimentar(id_alimento)
        if funcionou:
            jogador.guimoves -= 1
            jogador.save()
    return redirect(index)

def banheiro(request, id_guidu, id_banheiro):
    jogador = request.user.get_profile()
    guidu = get_object_or_404(Guidu, pk=id_guidu, jogador=jogador)
    if jogador.guimoves>0:
        funcionou = guidu.obrar(id_banheiro)
        if funcionou:
            jogador.guimoves -= 1
            jogador.save()
    return redirect(index)

def confortar(request, id_guidu, id_conforto):
    jogador = request.user.get_profile()
    guidu = get_object_or_404(Guidu, pk=id_guidu, jogador=jogador)
    if jogador.guimoves>0:
        funcionou = guidu.confortar(id_conforto)
        if funcionou:
            jogador.guimoves -= 1
            jogador.save()
    return redirect(index)

def banhar(request, id_guidu, id_banho):
    jogador = request.user.get_profile()
    guidu = get_object_or_404(Guidu, pk=id_guidu, jogador=jogador)
    if jogador.guimoves>0:
        funcionou = guidu.banhar(id_banho)
        if funcionou:
            jogador.guimoves -= 1
            jogador.save()
    return redirect(index)

def divertir(request, id_guidu, id_diversao):
    jogador = request.user.get_profile()
    guidu = get_object_or_404(Guidu, pk=id_guidu, jogador=jogador)
    if jogador.guimoves>0:
        funcionou = guidu.divertir(id_diversao)
        if funcionou:
            jogador.guimoves -= 1
            jogador.save()
    return redirect(index)

def socializar(request, id_guidu, id_socializar):
    jogador = request.user.get_profile()
    guidu = get_object_or_404(Guidu, pk=id_guidu, jogador=jogador)
    if jogador.guimoves>0:
        funcionou = guidu.socializar(id_socializar)
        if funcionou:
            jogador.guimoves -= 1
            jogador.save()
    return redirect(index)

def recuperar_energia(request, id_guidu, id_energia):
    jogador = request.user.get_profile()
    guidu = get_object_or_404(Guidu, pk=id_guidu, jogador=jogador)
    if jogador.guimoves>0:
        funcionou = guidu.recuperar_energia(id_energia)
        if funcionou:
            jogador.guimoves -= 1
            jogador.save()
    return redirect(index)



