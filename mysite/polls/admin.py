from django.contrib import admin

from .models import Question,Choice,Produtos,Pedido

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ["nomeProduto", "valorProduto", "quantidadeProduto", "imagem"]

class PedidosAdmin(admin.ModelAdmin):
    list_display = ["produto", "qtdCompra", "endereco"]


admin.site.register(Produtos, ProdutosAdmin)
admin.site.register(Pedido, PedidosAdmin)