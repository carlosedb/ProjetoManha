# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import CharField, EmailField, DateTimeField, ForeignKey ,\
    DateField

# Create your models here.

class Concurso(models.Model):
    """ Dados do concurso """
    titulo = CharField(max_length=200)
    data = DateField()

class Candidato(models.Model):
    """Dados do candidato que pode inscrever-se em um concurso."""
    nome = CharField(max_length=100)
    email = EmailField()

class Inscricao(model.Model):
    """Inscrições de candidatos em concursos."""
    data_hora = DateTimeField(auto_now_add=True, blank=True)
    candidato = ForeignKey(Candidato)
    concurso = models.ForeignKey(Concurso)
    class Meta:
        # O mesmo candidato não pode inscrever-se duas vezes em um mesmo concurso
        # https://docs.djangoproject.com/en/dev/ref/models/options/#unique-together
        unique_together = ('candidato', 'concurso') 