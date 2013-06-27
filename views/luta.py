from django.shortcuts import redirect, render_to_response, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext

from guidu.models import GuiduTipo, Guidu
from golpe.models import Golpe, Livro

@login_required
def lutar(request, id_guidu, id_guidu_alvo):    

    jogador = request.user.get_profile()
    guidu = get_object_or_404(Guidu, pk=id_guidu)    
    guidu_alvo = get_object_or_404(Guidu, pk=id_guidu_alvo)    
    
    #verifica se o jogador e o alvo sao a mesma pessoa
    if jogador == alvo:
        return redirect('pagina_de_alvos')
    
    
    #verifica se a experiencia do alvo eh menor que 60% da experiencia do atacante
    if jogador.experiencia * 0.6 > alvo.experiencia:
        return redirect(alvos)
    
    
    #atualiza o alvo e o jogador
    alvo.refresh()
    jogador.refresh()
    
    
    #verifica se o nosso jogador possui raiva para atacar
    if jogador.raiva_atual == 0:
        return redirect(alvos)
    
    
    #verifica se o nosso jogador esta "morto"
    if jogador.hp == 0:
        return redirect(alvos)
    
    #verifica se o alvo esta 'morto'
    if alvo.hp == 0:
        return redirect(alvos)
    
    
    #salva o hp inicial do jogador e do alvo para fazer um pequeno relatorio no final
    jogador_hp = jogador.hp
    alvo_hp = alvo.hp
    
    
    #pega o valor da arma do jogador
    if jogador.arma_ativa:
        jogador_arma = jogador.arma_ativa.poder
    else:
        jogador_arma = 1
    
    #pega o valor da armadura do jogador
    if jogador.armadura_ativa:
        jogador_armadura = jogador.armadura_ativa.poder
    else:
        jogador_armadura = 1
    
    
    #pega o valor da arma do alvo
    if alvo.arma_ativa:
        alvo_arma = alvo.arma_ativa.poder
    else:
        alvo_arma = 1
    
    #pega o valor da armadura do alvo
    if alvo.armadura_ativa:
        alvo_armadura = alvo.armadura_ativa.poder
    else:
        alvo_armadura = 1
    
    
    #agora o bicho vai pegar!
    #a luta dura 5 turnos
    for turno in [1, 2, 3, 4, 5]:
        #primeiro o jogador ataca
        ataque = randint(jogador.ataque/3, jogador.ataque)
        defesa = randint(alvo.defesa/3, alvo.defesa)
        
        #calcula o dano
        dano = ataque * jogador_arma - defesa * alvo_armadura
        
        if dano > 0:
            alvo.hp = alvo.hp - dano
        
        
        #agora o alvo ataca
        ataque = randint(alvo.ataque/3, alvo.ataque)
        defesa = randint(jogador.defesa/3, jogador.defesa)
        
        #calcula o dano
        dano = ataque * alvo_arma - defesa * jogador_armadura
        
        if dano > 0:
            jogador.hp = jogador.hp - dano
        
        
        #verifica se alguem morreu no combate
        if jogador.hp == 0 or alvo.hp == 0:
            break
    
    
    #descobrindo quem perdeu
    if jogador.hp == 0:
        vitoria = False
    elif alvo.hp == 0:
        vitoria = True
    elif alvo_hp - alvo.hp > jogador_hp - jogador.hp:
        vitoria = True
    else:
        vitoria = False
    
    
    #se o jogador ganhou, tira dinheiro do alvo e da ao jogador
    if vitoria:
        grana = alvo.carteira * ( randint(10, 90)/100.0 ) #entre 10% e 90% do valor da carteira
        grana = round(grana)
        
        alvo.carteira = alvo.carteira - grana
        jogador.carteira = jogador.carteira + grana
        
        #ganha 10% da experiencia do adversario
        jogador.experiencia = jogador.experiencia + alvo.experiencia * 0.1
    else:
        grana = jogador.carteira * ( randint(10, 90)/100.0 ) #entre 10% e 90% do valor da carteira
        grana = round(grana)
        
        alvo.carteira = alvo.carteira + grana
        jogador.carteira = jogador.carteira - grana
        
        #ganha 10% da experiencia do adversario
        alvo.experiencia = alvo.experiencia + jogador.experiencia * 0.1
    
    
    # o nosso atacante perde 1 de raiva
    jogador.raiva_atual = jogador.raiva_atual - 1
    
    
    #verifica se alguem deu level up
    alvo.level_up()
    jogador.level_up()
    
    
    #salva todas as alteracoes no banco de dados
    alvo.save()
    jogador.save()
    
    
    #exibe o template com o resultado da luta
    return render_to_response("atacar.html", {"player": jogador,
                                              "vida": jogador.vida * 10,
                                              "alvo": alvo,
                                              "vitoria": vitoria,
                                              "grana": grana,
                                              "jogador_hp": jogador_hp,
                                              "alvo_hp": alvo_hp})