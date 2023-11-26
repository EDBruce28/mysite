from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .forms import formPedido
from .models import Choice, Question, Produtos, Pedido

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "listaProdutos"

    def get_queryset(self):
        """Return the last five published questions."""
        return Produtos.objects.order_by("-valorProduto")[:5]


class DetailView(generic.DetailView):
    model = Produtos
    template_name = "polls/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formulario'] = formPedido(instance=self.object)
        return context


class ResultsView(generic.DetailView):
    model = Produtos
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

def compra(request, produto_id):
    produto = get_object_or_404(Produtos, pk=produto_id)
    if request.method == 'POST':
        formulario = formPedido(request.POST)

        if formulario.is_valid():
            # Salva os dados no banco de dados
            novo_objeto = formulario.save()

            # Você pode fazer algo com o novo objeto, se necessário

            # Redireciona para alguma página de sucesso
            return HttpResponseRedirect(reverse("polls:results", args=(produto.id,)))
    else:
        formulario = MeuFormulario()

    return render(
            request,
            "polls/detail.html",
            {
                "produto": produto,
                "error_message": "You didn't select a choice.",
            },
        )