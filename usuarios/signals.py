from django.contrib.auth.models import User
from django.db.models.signals import post_save
from usuarios.views import envia_email_quando_cria_usuario


def email_confirmacao_de_cadastro(sender, instance, created, **kwargs):
    if created:
        envia_email_quando_cria_usuario(instance.first_name, instance.email)


post_save.connect(email_confirmacao_de_cadastro, sender=User)
