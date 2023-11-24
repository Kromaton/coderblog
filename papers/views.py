from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from papers.models import Articulo
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class ArticuloListView(ListView):
    model = Articulo
    template_name = 'papers/articulos.html'
    


class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ('titulo', 'subtitulo', 'contenido')
    success_url = reverse_lazy('listar')
    
    def form_valid(self, form):
        self.object = form.save()
        # Agregamos la información del creador
        self.object.autor = self.request.user.username
        self.object.save()
        return super().form_valid(form)

class ArticuloDetailView(DetailView):
    model = Articulo
    fields = ('titulo', 'subtitulo', 'contenido', 'autor', 'creado', 'modificado')
    success_url = reverse_lazy('listar')
    
class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    fields = ('titulo', 'subtitulo', 'contenido')
    success_url = reverse_lazy('listar')

class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('listar')

@login_required
def listar_mis_articulos(request):
    # Data de pruebas, más adelante la llenaremos con nuestros cursos de verdad
    contexto = {
        "articulos": Articulo.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='papers/mis_articulos.html',
        context=contexto,
    )
    return http_response