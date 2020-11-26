from django.contrib import admin
from .forms import Produto_formulario

# Register your models here.

from .models import Produto, Estampa

class Produto_admin(admin.ModelAdmin):
    list_display = ['nome_do_cliente', 'estampa', 'valor_total']
    form = Produto_formulario
    list_filter = ['nome_do_cliente']
    search_fields = ['nome_do_cliente', 'estampa']

admin.site.register(Produto, Produto_admin)
