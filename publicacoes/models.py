from django.db import models
from django.contrib.auth.models import User

class Imagem(models.Model):
    class Meta:
        verbose_name = "Imagem da Galeria"
        verbose_name_plural = "Imagens da Galeria"

    titulo = models.CharField("titulo da imagem", max_length=50)
    imagem = models.FileField("Imagem", upload_to="static/galeria/", null=True, blank=True)

    def __str__(self):
        return self.titulo


class CapaPrincipal(models.Model):
    class Meta:
        verbose_name = "Capa Principal"
        verbose_name_plural = "Capas Principais"

    nome = models.CharField("Nome da Capa", max_length=150)
    imagem = models.FileField("Imagem da capa", upload_to="static/imagens/", null=True, blank=True)

    def __str__(self):
        return self.nome + "ID: ["+str(self.pk)+"]"


class Publicacoes(models.Model):
    class Meta:
        verbose_name = "Publicação"
        verbose_name_plural = "Publicações"

    titulo = models.CharField("Titulo do post", max_length=250)
    conteudo = models.TextField("Conteúdo do post", max_length=5000, null=True, blank = True)
    img_capa = models.CharField("Imagem de Capa", max_length=2500, null=True, blank=True)
    autor = models.ForeignKey(User, related_name="Autor", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return "ID [{}] - POST: {} de {}".format(self.pk, self.titulo, self.autor.first_name)
    

