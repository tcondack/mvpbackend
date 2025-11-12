from django.db import models
from djongo import models
from bson import ObjectId

class Parque(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, db_column='_id')
    nome =models.CharField(max_length=120)
    descricao = models.TextField()
    localizacao = models.CharField(max_length=200)
    horario_funcionamento = models.CharField(max_length=100)
    taxa_entrada = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    imagem = models.ImageField(upload_to='parques/', null=True, blank=True)
    def __str__(self):
        return self.nome

class Trilhas(models.Model):
    parque_id = models.ObjectIdField(primary_key=True, default=ObjectId, db_column='_id')
    nome = models.CharField(max_length=120)
    descricao = models.TextField()
    dificuldade = models.CharField(max_length=30, choices=[('Fácil', 'Fácil'), ('Médio', 'Médio'), ('Difícil', 'Difícil')])
    distancia = models.DecimalField(max_digits=5, decimal_places=2)
    imagem = models.ImageField(upload_to='trilhas/', null=True, blank=True)
    def __str__(self):
        return self.nome

class Eventos(models.Model):
    parque_id = models.ObjectIdField(primary_key=True, default=ObjectId, db_column='_id')
    nome = models.CharField(max_length=120)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    preco = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    imagem = models.ImageField(upload_to='eventos/', null=True, blank=True)
    def __str__(self):
        return self.nome