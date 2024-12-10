from django.shortcuts import render
from .models import Publicacoes, CapaPrincipal, Imagem


def Home(request):
    return render(request, 'home.html', {
        "ultimasPublicacoes": [],
        "img_capa": CapaPrincipal.objects.get(pk=1),
        "galeria": Imagem.objects.all()
    })

def GaleriaAdm(request):
    return render(request, 'galeria_adm.html', {
        "imagens":Imagem.objects.all(),
    })