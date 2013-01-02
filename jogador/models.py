from django.db import models
from django.contrib.auth.models import User

import datetime
import pytz

# Create your models here.

class Jogador(models.Model):

    user = models.OneToOneField(User)

    guicoin = models.PositiveIntegerField(default=0)
    guimoves = models.PositiveSmallIntegerField(default=10)

    update_guimoves = models.DateTimeField(auto_now_add=True)

    def refresh(self):
    	agora = datetime.datetime.now(pytz.timezone('America/Recife'))
        periodo = self.get_periodo()

        if self.guimoves < 10:
            tempo = agora - self.update_guimoves
            updates = tempo.total_seconds() // periodo

            if updates > 0:
                self.guimoves = self.guimoves + updates
                if self.guimoves > 10:
                    self.guimoves = 10
                #agora que verificou o ultimo update de hp, atualiza a variavel fome_update
                #self.update_guimoves = agora
                self.update_guimoves = self.update_guimoves + datetime.timedelta(seconds=updates*periodo)
        else:
            #se nao existe nenhum update para fazer, atualiza o fome_update
            self.update_guimoves = agora

        self.save()

        

    def __unicode__(self):
        return self.user.username

    def qnto_falta_acao(self):
        self.refresh()
        agora = datetime.datetime.now(pytz.timezone('America/Recife'))
        periodo = self.get_periodo()
        return ((self.update_guimoves + datetime.timedelta(seconds=periodo)) - agora).seconds

    def get_periodo(self):
        return 120

def cria_user_jogador(sender, instance, created, **kwargs):
    if created:
        Jogador.objects.create(user=instance)

models.signals.post_save.connect(cria_user_jogador, sender=User) 