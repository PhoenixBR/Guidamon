from django.db import models
from jogador.models import Jogador

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

    esta_dormindo = models.BooleanField(default=False)
    esta_morto = models.BooleanField(default=False)

    data_nascimento = models.DateTimeField(auto_now_add=True)

    humor_update = models.DateTimeField(auto_now_add=True)
    humor = models.CharField(max_length=50, default="normal")
    
    def get_periodo_acordado(self):
        return {'periodo_fome':1080, 'periodo_higiene':2160, 
                'periodo_diversao':720, 'periodo_banheiro':1080, 
                'periodo_social':1080, 'periodo_energia':5760}
    def get_periodo_dormindo(self):
        return  {'periodo_fome':2880, 'periodo_higiene':2880, 
                'periodo_diversao':5760, 'periodo_banheiro':2880, 
                'periodo_social':5760, 'periodo_energia':2880}


    def refresh(self):
        
        self.calcular_humor() #calcula humor de agora
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

        self.calcular_humor() #calcula humor de agora
        #self.save() #ja tem save no calcular_humor()


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

        self.refresh()
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
                self.save()
            return "triste"
        elif (calc_humor/qntd_atributos) >= 8:
            if self.humor != "feliz":
                self.humor = "feliz"
                self.humor_update = datetime.datetime.now(pytz.timezone(u'America/Recife'))
                self.save()
            return "feliz"
        else:
            if self.humor != "normal":
                self.humor = "normal"
                self.humor_update = datetime.datetime.now(pytz.timezone(u'America/Recife'))
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
        self.refresh()
        agora = datetime.datetime.now(pytz.timezone('America/Recife'))
        if self.esta_dormindo:
            periodo = self.get_periodo_dormindo()
        else:
            periodo = self.get_periodo_acordado()
        return ((self.fome_update + datetime.timedelta(seconds=periodo['periodo_fome'])) - agora).seconds

    def qnto_falta_higiene(self):
        self.refresh()
        agora = datetime.datetime.now(pytz.timezone('America/Recife'))
        if self.esta_dormindo:
            periodo = self.get_periodo_dormindo()
        else:
            periodo = self.get_periodo_acordado()
        return ((self.higiene_update + datetime.timedelta(seconds=periodo['periodo_higiene'])) - agora).seconds

    def qnto_falta_diversao(self):
        self.refresh()
        agora = datetime.datetime.now(pytz.timezone('America/Recife'))
        if self.esta_dormindo:
            periodo = self.get_periodo_dormindo()
        else:
            periodo = self.get_periodo_acordado()
        return ((self.diversao_update + datetime.timedelta(seconds=periodo['periodo_diversao'])) - agora).seconds

    def qnto_falta_banheiro(self):
        self.refresh()
        agora = datetime.datetime.now(pytz.timezone('America/Recife'))
        if self.esta_dormindo:
            periodo = self.get_periodo_dormindo()
        else:   
            periodo = self.get_periodo_acordado()
        return ((self.banheiro_update + datetime.timedelta(seconds=periodo['periodo_banheiro'])) - agora).seconds

    def qnto_falta_social(self):
        self.refresh()
        agora = datetime.datetime.now(pytz.timezone('America/Recife'))
        if self.esta_dormindo:
            periodo = self.get_periodo_dormindo()
        else:
            periodo = self.get_periodo_acordado()
        return ((self.social_update + datetime.timedelta(seconds=periodo['periodo_social'])) - agora).seconds

    def qnto_falta_energia(self):
        self.refresh()
        agora = datetime.datetime.now(pytz.timezone('America/Recife'))
        if self.esta_dormindo:
            periodo = self.get_periodo_dormindo()
        else:
            periodo = self.get_periodo_acordado()
        return ((self.energia_update + datetime.timedelta(seconds=periodo['periodo_energia'])) - agora).seconds

def define_humor_inicial(sender, instance, created, **kwargs):
    if created:
        instance.humor = instance.calcular_humor()
        '''instance.humor_update = datetime.datetime.now(pytz.timezone('America/Recife')) 
        instance.humor_update = instance.humor_update.astimezone(pytz.timezone('America/Recife'))
        instance.save()
        print instance.humor_update'''


models.signals.post_save.connect(define_humor_inicial, sender=Guidu) 


            
