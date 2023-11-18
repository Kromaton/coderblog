from django.shortcuts import render

# Create your views here.

def index(request):
    contexto = {
        'pagina' : 'index',
    }
    http_response = render(
        request=request,
        template_name='index.html',
        context=contexto,
    )
    return http_response

def acerca(request):
    contexto = {
        'pagina' : 'acerca',
    }
    http_response = render(
        request=request,
        template_name='acerca.html',
        context=contexto,
    )
    return http_response