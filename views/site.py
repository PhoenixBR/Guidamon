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
        return render_to_response("index.html", {"guidus": guidus})
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
    guidu.alimentar(id_alimento)
    return redirect(index)



