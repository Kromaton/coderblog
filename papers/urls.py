from django.urls import path
from papers.views import ArticuloListView, ArticuloCreateView, ArticuloDetailView, ArticuloUpdateView, ArticuloDeleteView, listar_mis_articulos

urlpatterns = [
    path('all/',                    ArticuloListView.as_view(),         name='listar'),
    path("my-blog/",                listar_mis_articulos,               name="miLista"),
    path('write/',                  ArticuloCreateView.as_view(),       name='crear'),
    path('detail/<int:pk>/',        ArticuloDetailView.as_view(),       name='detalle'),
    path('edit/<int:pk>/',          ArticuloUpdateView.as_view(),       name='editar'),
    path('delete/<int:pk>/',        ArticuloDeleteView.as_view(),       name='eliminar'),
]