"""little_ugly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pedidos_feios import views

urlpatterns = [
    path('admin_littleUgly/', admin.site.urls),
    path('', views.home, name='base'),
    path('add_pedido/', views.add_pedido, name='add_pedido'),
    path('pedidos/', views.lista_pedidos, name='pedidos'),
    path('update_pedido/<str:pk>', views.update_pedido, name="update_pedido"),
    path('delete_pedido/<str:pk>/', views.delete_pedido, name="delete_pedido"),
    path('detalhe_pedido/<str:pk>/', views.detalhe_pedido, name="detalhe_pedido"),
    path('accounts/', include('registration.backends.default.urls')),
    path('add_estampa/', views.add_estampa, name='add_estampa'),
    path('add_tamanho/', views.add_tamanho, name='add_tamanho'),
    path('add_modelo/', views.add_modelo, name='add_modelo'),
    path('add_pagamento/', views.add_pagamento, name='add_pagamento'),
    path('add_tipo_de_frete/', views.add_tipo_de_frete, name='add_tipo_de_frete'),
    path('add_canal_da_venda/', views.add_canal_da_venda, name='add_canal_da_venda'),
]
