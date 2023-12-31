# Generated by Django 4.2.4 on 2023-09-27 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=75, unique=True)),
                ('empresa_desenvolvedora', models.CharField(max_length=50)),
                ('ano_lancamento', models.IntegerField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plataforma', models.CharField(max_length=20)),
                ('jogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nome_jogo', to='jogos.jogos')),
            ],
        ),
    ]
