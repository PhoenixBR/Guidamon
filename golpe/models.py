from django.db import models

class Golpe(models.Model):

    nome = models.CharField(max_length=50, unique=True)
    poder = models.PositiveIntegerField(default=0)
    velocidade = models.PositiveIntegerField(default=0)
    nivel = models.PositiveSmallIntegerField(default=0)
    tipo = models.CharField(max_length=20)
    tempo_aprendizagem = models.PositiveIntegerField(default=7200)

    def __unicode__(self):
        return self.nome

class Livro(models.Model):

    nome = models.CharField(max_length=50, unique=True)
    preco = models.PositiveIntegerField(default=0)
    tipo = models.CharField(max_length=30)
    golpe = models.ManyToManyField(Golpe)

    def __unicode__(self):
        return self.nome