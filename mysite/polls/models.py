import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Produtos(models.Model):
    nomeProduto = models.CharField(max_length=200)
    valorProduto = models.DecimalField(max_digits=6, decimal_places=2)
    quantidadeProduto = models.IntegerField(default=0)
    imagem = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.nomeProduto

class Pedido(models.Model):
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    qtdCompra = models.IntegerField(default=0)
    endereco = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.produto