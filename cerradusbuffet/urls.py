from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from publicacoes.views import Home, GaleriaAdm

urlpatterns = [
    path('', Home, name="Home"),
    path('GaleriaAdm', GaleriaAdm, name="GaleriaAdm"),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
