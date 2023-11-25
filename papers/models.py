from django.db import models
from ckeditor.fields import RichTextField 

class Articulo(models.Model):
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=250)
    contenido = RichTextField(blank=True, null=True)
    autor = models.CharField(max_length=150)
    creado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='articulo', null=True, blank=True)