from django.contrib.auth.models import User
from django.db.models.signals import post_save


def email_confirmacao_de_cadastro(sender, instance, created, **kwargs):
    pass


# post_save(email_confirmacao_de_cadastro, sender=User)