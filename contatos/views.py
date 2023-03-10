from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.http import Http404
from django.core.paginator import Paginator
from django.shortcuts import render

def index(request):
    contatos = Contato.objects.all()
    paginator = Paginator(contatos,10)

    pageNumber = request.GET.get('page')
    contatos  = paginator.get_page(pageNumber)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def verContato(request, contato_id):
    contato = get_object_or_404(Contato, id = contato_id)

    if not contato.mostrar:
        raise Http404()
    
    return render(request, 'contatos/verContato.html', {
        'contato':contato
    })
