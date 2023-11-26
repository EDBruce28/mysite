# forms.py
from django import forms
from .models import Pedido

class formPedido (forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['produto','qtdCompra', 'endereco']
