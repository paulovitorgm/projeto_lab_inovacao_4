# Generated by Django 4.2.4 on 2023-09-29 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_remove_usuario_email_remove_usuario_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='disponivel_para_torneio',
            field=models.BooleanField(),
        ),
    ]
