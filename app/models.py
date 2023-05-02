from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Quantidade no estoque: ')

    def __str__(self):
        return str(self.nome)

