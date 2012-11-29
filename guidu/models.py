from django.db import models
from jogador.models import Jogador

import datetime
import pytz


class GuiduTipo(models.Model):

    nome_tipo = models.CharField(max_length=50)

    img_normal = models.ImageField(upload_to="guidutipo")
    img_feliz = models.ImageField(upload_to="guidutipo")
    img_triste = models.ImageField(upload_to="guidutipo")
    img_entediado = models.ImageField(upload_to="guidutipo")

    def __unicode__(self):
        return self.nome_tipo


class Guidu(models.Model):

    tipo = models.ForeignKey(GuiduTipo, null=False, related_name='+')
    jogador = models.ForeignKey(Jogador, null=True, related_name="guidus")

    nome = models.CharField(max_length=50, null=False)
    idade = models.PositiveSmallIntegerField(default=0)

    fome = models.PositiveSmallIntegerField(default=10)
    higiene = models.PositiveSmallIntegerField(default=10)
    diversao = models.PositiveSmallIntegerField(default=10)
    banheiro = models.PositiveSmallIntegerField(default=10)
    conforto = models.PositiveSmallIntegerField(default=10)
    social = models.PositiveSmallIntegerField(default=10)
    energia = models.PositiveSmallIntegerField(default=10)

    fome_update = models.DateTimeField(auto_now_add=True)
    higiene_update = models.DateTimeField(auto_now_add=True)
    diversao_update = models.DateTimeField(auto_now_add=True)
    banheiro_update = models.DateTimeField(auto_now_add=True)
    conforto_update = models.DateTimeField(auto_now_add=True)
    social_update = models.DateTimeField(auto_now_add=True)
    energia_update = models.DateTimeField(auto_now_add=True)

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

        if self.conforto > 0:
            tempo = agora - self.conforto_update
            updates = tempo.total_seconds() // 1080 #18min

            if updates > 0:
                self.conforto = self.conforto - updates
                if self.conforto < 0:
                    self.conforto = 0
                #agora que verificou o ultimo update de hp, atualiza a variavel fome_update
                self.conforto_update = agora
        else:
            #se nao existe nenhum update para fazer, atualiza o fome_update
            self.conforto_update = agora

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

    def alimentar(self, alimento):

        self.refresh()
        if(alimento == '1'):
            self.fome+=1
        elif(alimento == '2'):
            self.fome+=2
            self.banheiro-=1
        if(self.fome>10):
            self.fome=10

        self.save()

    def ir_banheiro(self, tipo_banheiro):

        self.refresh()
        if(tipo_banheiro == '1'):
            self.banheiro+=1
        if(self.banheiro>10):
            self.banheiro=10

        self.save()
        



