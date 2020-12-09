from django import forms
from .models import *
from little_ugly import settings


class Produto_formulario(forms.ModelForm):
    data_do_pedido = forms.DateField(required=False)
    class Meta:
        model = Produto
        fields = ['data_do_pedido', 'nome_do_cliente', 'canal_da_venda', 'modelo', 'estampa', 'tamanho',
                  'cor_do_tecido', 'cor_da_estampa', 'quantidade', 'modo_de_pagamento', 'pagamento_efetuado',
                  'frete', 'valor_do_frete', 'tipo_de_frete', 'valor_total', 'data_do_pedido_na_Mouse',
                  'data_da_finalizacao_na_Mouse', 'entregue', 'modo_de_entrega', 'observacao']

    def clean_nome_do_cliente(self):
        nome_do_cliente = self.cleaned_data.get('nome_do_cliente')
        if not nome_do_cliente:
            raise forms.ValidationError('Esse campo precisa ser preenchido!')
        return nome_do_cliente

    def clean_data_do_pedido(self):
        data_do_pedido = self.cleaned_data.get('data_do_pedido')
        if not data_do_pedido:
            raise forms.ValidationError('Esse campo precisa ser preenchido!')
        return data_do_pedido


class Produto_busca_filtro(forms.ModelForm):
    export_to_csv = forms.BooleanField(required=False)
    data_inicial = forms.DateField(required=False)
    data_final = forms.DateField(required=False)

    class Meta:
        model = Produto
        fields = ['nome_do_cliente', 'entregue', 'data_inicial', 'data_final']


class Produto_update(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['data_do_pedido', 'nome_do_cliente', 'canal_da_venda', 'modelo', 'estampa', 'tamanho',
                    'cor_do_tecido', 'cor_da_estampa', 'quantidade', 'modo_de_pagamento', 'pagamento_efetuado',
                    'frete', 'valor_do_frete', 'tipo_de_frete', 'valor_total', 'data_do_pedido_na_Mouse',
                    'data_da_finalizacao_na_Mouse', 'entregue', 'modo_de_entrega', 'observacao']


class EstampaCreateForm(forms.ModelForm):
    class Meta:
        model = Estampa
        fields = ['estampa']

class TamanhoCreateForm(forms.ModelForm):
    class Meta:
        model = Tamanho
        fields = ['tamanho']

class ModeloCreateForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ['modelo']

class ModoDePagamentoCreateForm(forms.ModelForm):
    class Meta:
        model = ModoDePagamento
        fields = ['modo_de_pagamento']

class TipoFreteCreateForm(forms.ModelForm):
    class Meta:
        model = TipoFrete
        fields = ['tipo_de_frete']

class CanalVendaCreateForm(forms.ModelForm):
	class Meta:
		model = CanalVenda
		fields = ['canal_da_venda']

class ModoEntregaCreateForm(forms.ModelForm):
	class Meta:
		model = ModoEntrega
		fields = ['modo_de_entrega']
