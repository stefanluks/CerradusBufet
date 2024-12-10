from django.contrib import admin
from .models import Publicacoes, CapaPrincipal, Imagem

admin.site.register(CapaPrincipal)
admin.site.register(Publicacoes)
admin.site.register(Imagem)
