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

    fome = models.PositiveSmallIntegerField(default=random.randint(2,8))
    higiene = models.PositiveSmallIntegerField(default=random.randint(2,8))
    diversao = models.PositiveSmallIntegerField(default=random.randint(2,8))
    banheiro = models.PositiveSmallIntegerField(default=random.randint(2,8))
    social = models.PositiveSmallIntegerField(default=random.randint(2,8))
    energia = models.PositiveSmallIntegerField(default=random.randint(2,8))

    fome_update = models.DateTimeField(auto_now_add=True)
    higiene_update = models.DateTimeField(auto_now_add=True)
    diversao_update = models.DateTimeField(auto_now_add=True)
    banheiro_update = models.DateTimeField(auto_now_add=True)
    social_update = models.DateTimeField(auto_now_add=True)
    energia_update = models.DateTimeField(auto_now_add=True)


    data_nascimento = models.DateTimeField(auto_now_add=True)

    humor = models.CharField(max_length=50, default="normal")
    

    def refresh(self):
        #pega a hora atual
        agora = datetime.datetime.now(pytz.timezone('America/Recife'))

        if self.fome > 0:
            tempo = agora - self.fome_update
            updates = tempo.total_seconds() // 1080 # 18min

            if updates > 0:
                self.fome = self.fome - updates
                if self.fome < 0:
                    self.fome = 0
                #agora que verificou o ultimo update de hp, atualiza a variavel fome_update
                self.fome_update = agora
        else:
            #se nao existe nenhum update para fazer, atualiza o fome_update
            self.fome_update = agora
         
        if self.higiene > 0:
            tempo = agora - self.higiene_update
            updates = tempo.total_seconds() // 2160 #36min

            if updates > 0:
                self.higiene = self.higiene - updates
                if self.higiene < 0:
                    self.higiene = 0
                #agora que verificou o ultimo update de hp, atualiza a variavel fome_update
                self.higiene_update = agora
        else:
            #se nao existe nenhum update para fazer, atualiza o fome_update
            self.higiene_update = agora

        if self.diversao > 0:
            tempo = agora - self.diversao_update
            updates = tempo.total_seconds() // 720

            if updates > 0:
                self.diversao = self.diversao - updates
                if self.diversao < 0:
                    self.diversao = 0
                #agora que verificou o ultimo update de hp, atualiza a variavel fome_update
                self.diversao_update = agora
        else:
            #se nao existe nenhum update para fazer, atualiza o fome_update
            self.diversao_update = agora

        if self.banheiro > 0:
            tempo = agora - self.banheiro_update
            updates = tempo.total_seconds() // 1080 #18min

            if updates > 0:
                self.banheiro = self.banheiro - updates
                if self.banheiro < 0:
                    self.banheiro = 0
                #agora que verificou o ultimo update de hp, atualiza a variavel fome_update
                self.banheiro_update = agora
        else:
            #se nao existe nenhum update para fazer, atualiza o fome_update
            self.banheiro_update = agora

        if self.social > 0:
            tempo = agora - self.social_update
            updates = tempo.total_seconds() // 1080 #18min

            if updates > 0:
                self.social = self.social - updates
                if self.social < 0:
                    self.social = 0
                #agora que verificou o ultimo update de hp, atualiza a variavel fome_update
                self.social_update = agora
        else:
            #se nao existe nenhum update para fazer, atualiza o fome_update
            self.social_update = agora

        if self.energia > 0:
            tempo = agora - self.energia_update
            updates = tempo.total_seconds() // 1080 #18min

            if updates > 0:
                self.energia = self.energia - updates
                if self.energia < 0:
                    self.energia = 0
                #agora que verificou o ultimo update de hp, atualiza a variavel fome_update
                self.energia_update = agora
        else:
            #se nao existe nenhum update para fazer, atualiza o fome_update
            self.energia_update = agora

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
        if self.fome <10:
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
        if self.banheiro <10:
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
        if self.higiene <10:
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
        if self.diversao <10:
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
        if self.social <10:
            if(tipo_socializacao == '1'):
                self.social+=7
            if(self.social>10):
                self.social=10

            self.save()
            funcionou = True
        return funcionou

    def recuperar_energia(self, tipo_energia):
        self.refresh()
        funcionou = False
        if self.energia <10:
            if(tipo_energia == '1'):
                self.energia+=5
            if(self.energia>10):
                self.energia=10

            self.save()
            funcionou = True
        return funcionou

    def calcular_humor(self):
        qntd_atributos = 6
        calc_humor = self.fome + self.higiene + self.diversao + self.banheiro + self.social + self.energia
        if (calc_humor/qntd_atributos) >= 8:
            return "feliz"
        elif (calc_humor/qntd_atributos) < 4 or self.atributo_baixo():
            return "triste"
        else:
            return "normal"

    def atributo_baixo(self):
        baixo = 4
        tem_baixo = False
        if self.humor <= baixo or self.higiene <= baixo or self.diversao <= baixo or self.banheiro <= baixo or self.social <= baixo or self.energia<= baixo:
            tem_baixo = True
        return tem_baixo