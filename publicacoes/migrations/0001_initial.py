# Generated by Django 5.0.7 on 2024-12-10 02:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250, verbose_name='Titulo do post')),
                ('conteudo', models.TextField(blank=True, max_length=5000, null=True, verbose_name='Conteúdo do post')),
                ('img_capa', models.CharField(blank=True, max_length=2500, null=True, verbose_name='Imagem de Capa')),
                ('autor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Autor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Publicação',
                'verbose_name_plural': 'Publicações',
            },
        ),
    ]