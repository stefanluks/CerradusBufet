# Generated by Django 5.0.7 on 2024-12-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacoes', '0004_alter_imagem_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacoes',
            name='resumo',
            field=models.TextField(blank=True, max_length=800, null=True, verbose_name='Resumo do post'),
        ),
    ]
