from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    title = "Little Ugly"
    context = {
        "title": title,
    }
    return render(request, 'base.html', context)

@login_required
def add_pedido(request):
    form = Produto_formulario(request.POST or None)
    if form.is_valid():
        form.save()

        return redirect('/pedidos')

    title = "Add Pedidos - Little Ugly"
    context = {
        "form": form,
        "title": title,
    }
    return render(request, 'add_pedido.html', context)

@login_required
def lista_pedidos(request):
    title = "Pedidos - Little Ugly"
    form = Produto_busca_filtro(request.POST or None)
    queryset = Produto.objects.all()

    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }

    if request.method == 'POST':
        queryset = Produto.objects.filter(nome_do_cliente__icontains = form['nome_do_cliente'].value(),
                                          modo_de_pagamento__exact = form['modo_de_pagamento'].value())


        if form['export_to_csv'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content Disposition'] = 'attachment: filename="Lista de Pedidos.csv"'
            writer = csv.writer(response)
            writer.writerow(['data_do_pedido', 'nome_do_cliente', 'canal_da_venda', 'modelo', 'estampa', 'tamanho',
                             'cor_do_tecido', 'cor_da_estampa', 'quantidade', 'modo_de_pagamento',
                             'pagamento_efetuado', 'frete', 'valor_do_frete', 'tipo_de_frete','valor_total',
                             'data_do_pedido_na_Mouse', 'data_da_finalizacao_na_Mouse', 'entregue', 'modo_de_entrega'])
            instance = queryset
            for produto in instance:
                writer.writerow([produto.data_do_pedido, produto.nome_do_cliente, produto.canal_da_venda, produto.modelo,
                                 produto.estampa, produto.tamanho, produto.cor_do_tecido, produto.cor_da_estampa, quantidade,
                                 produto.modo_de_pagamento, produto.pagamento_efetuado,
                                 produto.frete, produto.valor_do_frete, produto.tipo_de_frete, produto.valor_total,
                                 produto.data_do_pedido_na_Mouse, produto.data_da_finalizacao_na_Mouse, produto.entregue,
                                 produto.modo_de_entrega])
                return response

        context = {
            "title": title,
            "queryset": queryset,
            "form": form,
        }

    return render(request, 'pedidos.html', context)


def update_pedido(request, pk):
	queryset = Produto.objects.get(id=pk)
	form = Produto_update(instance=queryset)
	if request.method == 'POST':
		form = Produto_update(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/pedidos')

	context = {
		'form':form
	}
	return render(request, 'add_pedido.html', context)


def delete_pedido(request, pk):
	queryset = Produto.objects.get(id=pk)

	if request.method == 'POST':
		queryset.delete()
		return redirect('/pedidos')

	return render(request, 'delete_pedido.html')


def detalhe_pedido(request, pk):
	queryset = Produto.objects.get(id=pk)
	context = {
		"title": queryset.nome_do_cliente,
		"queryset": queryset,
	}
	return render(request, "detalhe_pedido.html", context)


def add_estampa(request):
	form = EstampaCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Estampa adicionada com Sucesso!')
		return redirect('/add_pedido')
	context = {
		"form": form,
		"title": "Add Estampa",
	}
	return render(request, "add_estampa.html", context)


def add_tamanho(request):
	form = TamanhoCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Tamanho adicionado com Sucesso!')
		return redirect('/add_pedido')
	context = {
		"form": form,
		"title": "Add Tamanho",
	}
	return render(request, "add_tamanho.html", context)


def add_modelo(request):
	form = ModeloCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Modelo adicionado com Sucesso!')
		return redirect('/add_pedido')
	context = {
		"form": form,
		"title": "Add Modelo",
	}
	return render(request, "add_modelo.html", context)


def add_pagamento(request):
	form = PagamentoCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Modo de Pagamento adicionado com Sucesso!')
		return redirect('/add_pedido')
	context = {
		"form": form,
		"title": "Add Pagamento",
	}
	return render(request, "add_pagamento.html", context)


def add_tipo_de_frete(request):
	form = TipoFreteCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Tipo de frete adicionado com Sucesso!')
		return redirect('/add_pedido')
	context = {
		"form": form,
		"title": "Add Tipo de Frete",
	}
	return render(request, "add_tipo_de_frete.html", context)


def add_canal_da_venda(request):
	form = CanalVendaCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Canal de venda adicionado com Sucesso!')
		return redirect('/add_canal_da_venda')
	context = {
		"form": form,
		"title": "Add Canal de Venda",
	}
	return render(request, "add_canal_da_venda.html", context)