from django.db import models
from jogador.models import Jogador
from golpe.models import Golpe

import datetime
import pytz
import random

class GuiduTipo(models.Model):

    nome_tipo = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nome_tipo


class Guidu(models.Model):

    tipo = models.ForeignKey(GuiduTipo, null=False, related_name='+')
    jogador = models.ForeignKey(Jogador, null=True, related_name="guidus")

    nome = models.CharField(max_length=50, null=False)

    fome = models.PositiveSmallIntegerField(default=2)
    higiene = models.PositiveSmallIntegerField(default=random.randint(2,8))
    diversao = models.PositiveSmallIntegerField(default=random.randint(2,8))
    banheiro = models.PositiveSmallIntegerField(default=random.randint(2,8))
    social = models.PositiveSmallIntegerField(default=random.randint(2,8))
    energia = models.PositiveSmallIntegerField(default=10)

    fome_update = models.DateTimeField(auto_now_add=True)
    higiene_update = models.DateTimeField(auto_now_add=True)
    diversao_update = models.DateTimeField(auto_now_add=True)
    banheiro_update = models.DateTimeField(auto_now_add=True)
    social_update = models.DateTimeField(auto_now_add=True)
    energia_update = models.DateTimeField(auto_now_add=True)

    ataque = models.PositiveSmallIntegerField(default=10)
    defesa = models.PositiveSmallIntegerField(default=10)
    dextreza = models.PositiveSmallIntegerField(default=10)
    magia = models.PositiveSmallIntegerField(default=10)
    vida = models.PositiveSmallIntegerField(default=10)

    hp = models.PositiveIntegerField(default=100) #hp = vida * 10 no max
    nivel = models.PositiveSmallIntegerField(default=1)
    experiencia = models.PositiveIntegerField(default=0)

    esta_dormindo = models.BooleanField(default=False)
    esta_morto = models.BooleanField(default=False)

    data_nascimento = models.DateTimeField(auto_now_add=True)

    humor_update = models.DateTimeField(auto_now_add=True)
    humor = models.CharField(max_length=50, default="normal")
    humor_guicoin = models.PositiveIntegerField(default=0)

    golpe_aprendido1 = models.ForeignKey(Golpe, null=True, blank=True, related_name="+")
    golpe_aprendido2 = models.ForeignKey(Golpe, null=True, blank=True, related_name="+")
    golpe_aprendido3 = models.ForeignKey(Golpe, null=True, blank=True, related_name="+")
    golpe_aprendido4 = models.ForeignKey(Golpe, null=True, blank=True, related_name="+")
    golpe_aprendido5 = models.ForeignKey(Golpe, null=True, blank=True, related_name="+")

    esta_treinando = models.BooleanField(default=False)
    golpe_treinando = models.ForeignKey(Golpe, null=True, blank=True, related_name="+") 
    golpe_treinando_desde = models.DateTimeField(null=True, blank=True)
    golpe_tempo_treinado = models.PositiveIntegerField(default=0)


    def get_periodo_acordado(self):
        return {'periodo_fome':1080, 'periodo_higiene':2160, 
                'periodo_diversao':720, 'periodo_banheiro':1080, 
                'periodo_social':1080, 'periodo_energia':5760}
    def get_periodo_dormindo(self):
        return  {'periodo_fome':2880, 'periodo_higiene':2880, 
                'periodo_diversao':5760, 'periodo_banheiro':2880, 
                'periodo_social':5760, 'periodo_energia':2880}


    def refresh(self):
        
        
        self.adiciona_moedas() #adiciona moedas antes de possivelmente alterar humor
        self.calcular_humor() #calcula humor de agora antes de verificar morte pq vai que o guidu melhorou...
        self.verificar_morte() #verifica se esta morto
        
        #pega a hora atual
        agora = datetime.datetime.now(pytz.timezone('America/Recife'))
        periodos_acordado = self.get_periodo_acordado()
        periodos_dormindo = self.get_periodo_dormindo()
       
        # Fome
        if self.fome > 0:
            tempo = agora - self.fome_update
            if self.esta_dormindo:
                updates = tempo.total_seconds() // periodos_dormindo['periodo_fome']
            else:
                updates = tempo.total_seconds() // periodos_acordado['periodo_fome']

            if updates > 0:
                self.fome = self.fome - updates
                if self.fome < 0:
                    self.fome = 0
                    #agora que verificou o ultimo update de hp, atualiza a variavel fome_update
                if self.esta_dormindo:
                    self.fome_update = self.fome_update + datetime.timedelta(seconds=updates*periodos_dormindo['periodo_fome'])
                else:
                    self.fome_update = self.fome_update + datetime.timedelta(seconds=updates*periodos_acordado['periodo_fome'])
        else:
            #se nao existe nenhum update para fazer, atualiza o fome_update
            self.fome_update = agora
        
        # Higiene
        if self.higiene > 0:
            tempo = agora - self.higiene_update
            if self.esta_dormindo:
                updates = tempo.total_seconds() // periodos_dormindo['periodo_higiene']
            else:
                updates = tempo.total_seconds() // periodos_acordado['periodo_higiene']

            if updates > 0:
                self.higiene = self.higiene - updates
                if self.higiene < 0:
                    self.higiene = 0
                    #agora que verificou o ultimo update de hp, atualiza a variavel higiene_update
                if self.esta_dormindo:
                    self.higiene_update = self.higiene_update + datetime.timedelta(seconds=updates*periodos_dormindo['periodo_higiene'])
                else:
                    self.higiene_update = self.higiene_update + datetime.timedelta(seconds=updates*periodos_acordado['periodo_higiene'])
        else:
            #se nao existe nenhum update para fazer, atualiza o higiene_update
            self.higiene_update = agora

        # Diversao
        if self.diversao > 0:
            tempo = agora - self.diversao_update
            if self.esta_dormindo:
                updates = tempo.total_seconds() // periodos_dormindo['periodo_diversao']
            else:
                updates = tempo.total_seconds() // periodos_acordado['periodo_diversao']

            if updates > 0:
                self.diversao = self.diversao - updates
                if self.diversao < 0:
                    self.diversao = 0
                    #agora que verificou o ultimo update de hp, atualiza a variavel diversao_update
                if self.esta_dormindo:
                    self.diversao_update = self.diversao_update + datetime.timedelta(seconds=updates*periodos_dormindo['periodo_diversao'])
                else:
                    self.diversao_update = self.diversao_update + datetime.timedelta(seconds=updates*periodos_acordado['periodo_diversao'])
        else:
            #se nao existe nenhum update para fazer, atualiza o fome_update
            self.diversao_update = agora

        # Banheiro
        if self.banheiro > 0:
            tempo = agora - self.banheiro_update
            if self.esta_dormindo:
                updates = tempo.total_seconds() // periodos_dormindo['periodo_banheiro']
            else:
                updates = tempo.total_seconds() // periodos_acordado['periodo_banheiro']

            if updates > 0:
                self.banheiro = self.banheiro - updates
                if self.banheiro < 0:
                    self.banheiro = 0
                #agora que verificou o ultimo update de hp, atualiza a variavel banheiro_update
                if self.esta_dormindo:
                    self.banheiro_update = self.banheiro_update + datetime.timedelta(seconds=updates*periodos_dormindo['periodo_banheiro'])
                else:
                    self.banheiro_update = self.banheiro_update + datetime.timedelta(seconds=updates*periodos_acordado['periodo_banheiro'])
        else:
            #se nao existe nenhum update para fazer, atualiza o banheiro_update
            self.banheiro_update = agora

        # Social
        if self.social > 0:
            tempo = agora - self.social_update
            if self.esta_dormindo:
                updates = tempo.total_seconds() // periodos_dormindo['periodo_social']
            else:
                updates = tempo.total_seconds() // periodos_acordado['periodo_social']

            if updates > 0:
                self.social = self.social - updates
                if self.social < 0:
                    self.social = 0
                #agora que verificou o ultimo update de hp, atualiza a variavel social_update
                if self.esta_dormindo:
                    self.social_update = self.social_update + datetime.timedelta(seconds=updates*periodos_dormindo['periodo_social'])
                else:
                    self.social_update = self.social_update + datetime.timedelta(seconds=updates*periodos_acordado['periodo_social'])
        else:
            #se nao existe nenhum update para fazer, atualiza o social_update
            self.social_update = agora

        # Energia
        if self.esta_dormindo:
            if self.energia < 10:
                tempo = agora - self.energia_update
                updates = tempo.total_seconds() // periodos_dormindo['periodo_energia']

                if updates > 0:
                    self.energia = self.energia + updates
                    if self.energia >= 10:
                        self.energia = 10
                        self.acordar()
                    #agora que verificou o ultimo update de hp, atualiza a variavel energia_update
                    self.energia_update = self.energia_update + datetime.timedelta(seconds=updates*periodos_dormindo['periodo_energia'])
            else:
                #se nao existe nenhum update para fazer, atualiza o energia_update
                self.update_guimoves = agora
        else:
            if self.energia > 0:
                tempo = agora - self.energia_update
                updates = tempo.total_seconds() // periodos_acordado['periodo_energia']

                if updates > 0:
                    self.energia = self.energia - updates
                    if self.energia < 0:
                        self.energia = 0
                    #agora que verificou o ultimo update de hp, atualiza a variavel fome_update
                    self.energia_update = self.energia_update + datetime.timedelta(seconds=updates*periodos_acordado['periodo_energia'])
            else:
                #se nao existe nenhum update para fazer, atualiza o fome_update
                self.energia_update = agora

        self.verifica_termino_treino()
        self.calcular_humor() #calcula humor denovo pra saber se alterou depois das mudancas.
        self.save()

    def __unicode__(self):
        return self.nome

    def saber_idade_segundos(self):
        agora = datetime.datetime.now(pytz.timezone('America/Recife'))
        idade = (agora - self.data_nascimento).seconds
        return idade

    def saber_idade_dias(self):
        agora = datetime.datetime.now(pytz.timezone('America/Recife'))
        idade = (agora - self.data_nascimento).days
        return idade

    def alimentar(self, alimento):

        self.refresh() #da refresh antes pra pegar o estado mais atual do guidu
        funcionou = False
        if self.fome <10 and (not self.esta_dormindo):
            if(alimento == '1'):
                self.fome+=1
            elif(alimento == '2'):
                self.fome+=2
                if self.banheiro>=1:
                    self.banheiro-=1
            if(self.fome>10):
                self.fome=10

            self.save()
            funcionou = True
        return funcionou

    def obrar(self, tipo_banheiro):

        self.refresh()
        funcionou = False
        if self.banheiro <10 and (not self.esta_dormindo):
            if(tipo_banheiro == '1'):
                self.banheiro+=3
                if self.higiene >=1:
                    self.higiene-=1
            if(self.banheiro>10):
                self.banheiro=10

            self.save()
            funcionou = True
        return funcionou

    def banhar(self, tipo_banho):
        self.refresh()
        funcionou = False
        if self.higiene <10 and (not self.esta_dormindo):
            if(tipo_banho == '1'):
                self.higiene+=4
            if(self.higiene>10):
                self.higiene=10

            self.save()
            funcionou = True
        return funcionou

    def divertir(self, tipo_diversao):
        self.refresh()
        funcionou = False
        if self.diversao <10 and (not self.esta_dormindo):
            if(tipo_diversao == '1'):
                self.diversao+=3
            if(self.diversao>10):
                self.diversao=10

            self.save()
            funcionou = True
        return funcionou

    def socializar(self, tipo_socializacao):
        self.refresh()
        funcionou = False
        if self.social <10 and (not self.esta_dormindo):
            if(tipo_socializacao == '1'):
                self.social+=7
            if(self.social>10):
                self.social=10

            self.save()
            funcionou = True
        return funcionou

    def calcular_humor(self):
        
        qntd_atributos = 6
        calc_humor = self.fome + self.higiene + self.diversao + self.banheiro + self.social + self.energia
        
        if ((calc_humor/qntd_atributos) < 4 or self.atributo_baixo()):
            if self.humor != "triste":
                self.humor = "triste"
                self.humor_update = datetime.datetime.now(pytz.timezone(u'America/Recife'))
                self.humor_guicoin = 0
                self.save()
            return "triste"
        elif (calc_humor/qntd_atributos) >= 8:
            if self.humor != "feliz":
                self.humor = "feliz"
                self.humor_update = datetime.datetime.now(pytz.timezone(u'America/Recife'))
                self.humor_guicoin = 0
                self.save()
            return "feliz"
        else:
            if self.humor != "normal":
                self.humor = "normal"
                self.humor_update = datetime.datetime.now(pytz.timezone(u'America/Recife'))
                self.humor_guicoin = 0
                self.save()
            return "normal"

    def atributo_baixo(self):
        baixo = 2
        tem_baixo = False
        if self.fome <= baixo or self.higiene <= baixo or self.diversao <= baixo or self.banheiro <= baixo or self.social <= baixo or self.energia<= baixo:
            tem_baixo = True
        return tem_baixo

    def dormir(self):
        self.refresh()
        funcionou = False
        if self.energia <10 and self.esta_dormindo == False:
            self.esta_dormindo = True
            self.energia_update = datetime.datetime.now(pytz.timezone('America/Recife'))
            self.save()
            funcionou = True
        return funcionou

    def acordar(self):
        self.refresh()
        funcionou = False
        if self.esta_dormindo == True:
            self.esta_dormindo = False
            self.energia_update = datetime.datetime.now(pytz.timezone('America/Recife'))
            self.save()
            funcionou = True
        return funcionou

    def verificar_morte(self):
        if self.humor == "triste":
            agora = datetime.datetime.now(pytz.timezone('America/Recife'))
            dias_de_tristeza = (agora - self.humor_update).days
            if dias_de_tristeza >= 1:
                self.esta_morto = True
                self.save()
        return self.esta_morto

    def qnto_falta_fome(self):
        
        #self.refresh() #esse refresh pode ser tirado se prometer ser logo depois de carregar a pagina (e dar refresh)
        agora = datetime.datetime.now(pytz.timezone('America/Recife'))
        if self.esta_dormindo:
            periodo = self.get_periodo_dormindo()
        else:
            periodo = self.get_periodo_acordado()
        timedelta = ((self.fome_update + datetime.timedelta(seconds=periodo['periodo_fome'])) - agora)
        return str(datetime.timedelta(seconds=timedelta.seconds)) #o tempo sai no formato hh:mm:ss

    def qnto_falta_higiene(self):
        
        #self.refresh() #esse refresh pode ser tirado se prometer ser logo depois de carregar a pagina (e dar refresh)
        agora = datetime.datetime.now(pytz.timezone('America/Recife'))
        if self.esta_dormindo:
            periodo = self.get_periodo_dormindo()
        else:
            periodo = self.get_periodo_acordado()
        timedelta = ((self.higiene_update + datetime.timedelta(seconds=periodo['periodo_higiene'])) - agora)
        return str(datetime.timedelta(seconds=timedelta.seconds)) #o tempo sai no formato hh:mm:ss

    def qnto_falta_diversao(self):
        
        #self.refresh() #esse refresh pode ser tirado se prometer ser logo depois de carregar a pagina (e dar refresh)
        agora = datetime.datetime.now(pytz.timezone('America/Recife'))
        if self.esta_dormindo:
            periodo = self.get_periodo_dormindo()
        else:
            periodo = self.get_periodo_acordado()
        timedelta = ((self.diversao_update + datetime.timedelta(seconds=periodo['periodo_diversao'])) - agora)
        return str(datetime.timedelta(seconds=timedelta.seconds)) #o tempo sai no formato hh:mm:ss

    def qnto_falta_banheiro(self):
         
        #self.refresh() #esse refresh pode ser tirado se prometer ser logo depois de carregar a pagina (e dar refresh)
        agora = datetime.datetime.now(pytz.timezone('America/Recife'))
        if self.esta_dormindo:
            periodo = self.get_periodo_dormindo()
        else:   
            periodo = self.get_periodo_acordado()
        timedelta = ((self.banheiro_update + datetime.timedelta(seconds=periodo['periodo_banheiro'])) - agora)
        return str(datetime.timedelta(seconds=timedelta.seconds)) #o tempo sai no formato hh:mm:ss

    def qnto_falta_social(self):
        
        #self.refresh() #esse refresh pode ser tirado se prometer ser logo depois de carregar a pagina (e dar refresh)
        agora = datetime.datetime.now(pytz.timezone('America/Recife'))
        if self.esta_dormindo:
            periodo = self.get_periodo_dormindo()
        else:
            periodo = self.get_periodo_acordado()
        timedelta = ((self.social_update + datetime.timedelta(seconds=periodo['periodo_social'])) - agora)
        return str(datetime.timedelta(seconds=timedelta.seconds)) #o tempo sai no formato hh:mm:ss

    def qnto_falta_energia(self):
        
        #self.refresh() #esse refresh pode ser tirado se prometer ser logo depois de carregar a pagina (e dar refresh)
        agora = datetime.datetime.now(pytz.timezone('America/Recife'))
        if self.esta_dormindo:
            periodo = self.get_periodo_dormindo()
        else:
            periodo = self.get_periodo_acordado()
        timedelta = ((self.energia_update + datetime.timedelta(seconds=periodo['periodo_energia'])) - agora)
        return str(datetime.timedelta(seconds=timedelta.seconds)) #o tempo sai no formato hh:mm:ss

    def qnto_falta_treino(self):
        
        #self.refresh() #esse refresh pode ser tirado se prometer ser logo depois de carregar a pagina (e dar refresh)
        if self.golpe_treinando:
            agora = datetime.datetime.now(pytz.timezone('America/Recife'))
            tempo_total = self.golpe_treinando.tempo_aprendizagem
            if(self.esta_treinando):
                tempo_ja_aprendido = (agora-self.golpe_treinando_desde).seconds + self.golpe_tempo_treinado
            else:
                tempo_ja_aprendido = self.golpe_tempo_treinado
            qnto_falta = tempo_total - tempo_ja_aprendido
            return qnto_falta

    def adiciona_moedas(self):
        if(self.humor == 'feliz' or self.humor == 'normal'):
            periodo = 60 #1 min            
            agora = datetime.datetime.now(pytz.timezone('America/Recife'))
            update = (agora - self.humor_update).seconds/periodo
            if update > 0:
                if update > self.humor_guicoin:
                    if self.humor == 'feliz':
                        moedas = 10
                    else:
                        moedas = 5
                    
                    self.jogador.guicoin = self.jogador.guicoin + (moedas*(update-self.humor_guicoin))
                    self.jogador.save()
                    self.humor_guicoin = update
                    self.save()

    def verifica_termino_treino(self):
        if self.esta_treinando:
            periodo = self.golpe_treinando.tempo_aprendizagem            
            agora = datetime.datetime.now(pytz.timezone('America/Recife'))
            tempo_treinando = (agora - self.golpe_treinando_desde).seconds + self.golpe_tempo_treinado
            if(tempo_treinando>=periodo):
                
                #tem que ter certeza que ha pelo menos um slot livre
                #na hora que (re)comecar a treinar, tem que garantir isso.
                if(self.golpe_aprendido1==None): self.golpe_aprendido1 = self.golpe_treinando
                elif(self.golpe_aprendido2==None): self.golpe_aprendido2 = self.golpe_treinando
                elif(self.golpe_aprendido3==None): self.golpe_aprendido3 = self.golpe_treinando

                self.parar_treino()

    def pausar_treino(self):
        
        agora = datetime.datetime.now(pytz.timezone('America/Recife'))
        self.golpe_tempo_treinado += (agora-self.golpe_treinando_desde).seconds
        self.golpe_treinando_desde = None
        self.esta_treinando = False
        #guidu.golpe_treinando ainda estara la, pra lembrar qual o golpe que estava treinando
        self.save()

    def parar_treino(self):
        self.esta_treinando = False
        self.golpe_treinando = None
        self.golpe_treinando_desde = None
        self.golpe_tempo_treinado = 0
        self.save()
        



    def comecar_treino(self, golpe):

        if(self.golpe_treinando==None):
            self.golpe_tempo_treinado = 0
            self.golpe_treinando = golpe

        self.golpe_treinando_desde = datetime.datetime.now(pytz.timezone('America/Recife'))
        self.esta_treinando = True
        self.save()

def define_humor_inicial(sender, instance, created, **kwargs):
    if created:
        instance.humor = instance.calcular_humor()
        '''instance.humor_update = datetime.datetime.now(pytz.timezone('America/Recife')) 
        instance.humor_update = instance.humor_update.astimezone(pytz.timezone('America/Recife'))
        instance.save()
        print instance.humor_update'''


models.signals.post_save.connect(define_humor_inicial, sender=Guidu) 


            
