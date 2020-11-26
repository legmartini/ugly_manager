from django.db import models
from little_ugly import settings

# Create your models here.


class Estampa(models.Model):
    nome_da_estampa = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nome_da_estampa

class Tamanho(models.Model):
    tamanho = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.tamanho

class Modelo(models.Model):
    modelo = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.modelo

class Pagamento(models.Model):
    pagamento = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.pagamento

class TipoFrete(models.Model):
    tipo_de_frete = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.tipo_de_frete

class CanalVenda(models.Model):
    canal_da_venda = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.canal_da_venda

class ModoEntrega(models.Model):
    modo_de_entrega = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.modo_de_entrega

class Produto(models.Model):

    opcoes = (
        ('Sim', 'Sim'),
        ('Não', 'Não')
    )

    data_do_pedido = models.DateField(blank=False)
    nome_do_cliente = models.CharField(max_length=64, null=True, blank=True)
    canal_da_venda = models.ForeignKey(CanalVenda, on_delete=models.CASCADE, blank=True, null=True)

    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, blank=True, null=True)
    estampa = models.ForeignKey(Estampa, on_delete=models.CASCADE, blank=True, null=True)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE, blank=True, null=True)
    cor_do_tecido = models.CharField(max_length=16, null=True, blank=True)
    cor_da_estampa = models.CharField(max_length=16, null=True, blank=True)
    quantidade = models.IntegerField(blank=False, null=True)

    modo_de_pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE, blank=True, null=True)
    pagamento_efetuado = models.CharField(max_length=8, null=True, choices=opcoes, default="Não", blank=False)
    frete = models.CharField(max_length=8, null=True, choices=opcoes, default="Não", blank=False)
    valor_do_frete = models.FloatField(blank=True, null=True)
    tipo_de_frete = models.ForeignKey(TipoFrete, on_delete=models.CASCADE, blank=True, null=True)
    valor_total = models.FloatField(blank=False, null=True)

    data_do_pedido_na_Mouse = models.DateField(null=True, blank=True)
    data_da_finalizacao_na_Mouse = models.DateField(null=True, blank=True)

    entregue = models.CharField(max_length=8, null=True, choices=opcoes, default="Não", blank=False)
    modo_de_entrega = models.ForeignKey(ModoEntrega, on_delete=models.CASCADE, blank=True, null=True)

    observacao = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return (f'{self.data_do_pedido}, {self.nome_do_cliente}')
