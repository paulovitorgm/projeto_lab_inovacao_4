# Generated by Django 4.2.4 on 2023-08-30 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0002_remove_usuario_senha'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='id_auth_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rel_usuario', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
