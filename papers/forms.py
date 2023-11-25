from django import forms
from papers.models import Articulo
from ckeditor.widgets import CKEditorWidget

class PostArticulo(forms.ModelForm):
    contenido = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Articulo
        fields = ('titulo',
                  'subtitulo',
                  'contenido',
                  'imagen',
        )