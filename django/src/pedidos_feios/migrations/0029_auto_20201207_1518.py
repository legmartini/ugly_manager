# Generated by Django 3.1.2 on 2020-12-07 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos_feios', '0028_auto_20201127_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canalvenda',
            name='canal_da_venda',
            field=models.CharField(blank=True, default='0', max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='estampa',
            name='estampa',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='modelo',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='mododepagamento',
            name='modo_de_pagamento',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='modoentrega',
            name='modo_de_entrega',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tamanho',
            name='tamanho',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tipofrete',
            name='tipo_de_frete',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
