from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Jogador(models.Model):

    user = models.OneToOneField(User)

    guicoin = models.PositiveIntegerField(default=0)
    guimoves = models.PositiveSmallIntegerField(default=10)

    def __unicode__(self):
        return self.user.username



def cria_user_jogador(sender, instance, created, **kwargs):
    if created:
        Jogador.objects.create(user=instance)

models.signals.post_save.connect(cria_user_jogador, sender=User) 