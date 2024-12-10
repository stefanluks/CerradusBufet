# Generated by Django 5.0.7 on 2024-12-10 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CapaPrincipal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome da Capa')),
                ('imagem', models.FileField(blank=True, null=True, upload_to='static/imagens/', verbose_name='Imagem da capa')),
            ],
            options={
                'verbose_name': 'Capa Principal',
                'verbose_name_plural': 'Capas Principais',
            },
        ),
    ]
