# Generated by Django 5.0.7 on 2024-12-10 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacoes', '0003_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='imagem',
            field=models.FileField(blank=True, null=True, upload_to='static/galeria/', verbose_name='Imagem'),
        ),
    ]