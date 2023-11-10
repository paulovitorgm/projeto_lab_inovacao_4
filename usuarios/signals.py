from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from usuarios.models import Usuario
from usuarios.views import enviar_email


@receiver(post_save, sender=User)
def email_criacao_de_cadastro(sender, instance, created, **kwargs):
    if created:
        envia_email_quando_cria_usuario(instance.first_name, instance.email)


@receiver(post_save, sender=User)
def email_alteracao_de_cadastro(sender, instance, created, **kwargs):
    if not created and kwargs.get('update_fields') and not ("last_login" in kwargs.get('update_fields')):
         envia_email_quando_altera_usuario(instance.first_name, instance.email)


@receiver(post_save, sender=Usuario)
def email_alteracao_usuario(sender, instance, created, **kwargs):
    if not created and kwargs.get('update_fields'):
        usuario = User.objects.get(pk=instance.id_usuario_id)
        # usuario = User.objects.filter(pk=instance.id_usuario_id).first()
        envia_email_quando_altera_usuario(usuario.first_name, usuario.email)
        print(kwargs)


def envia_email_quando_cria_usuario(nome, destinatario):
    assunto = "Criação de conta"
    mensagem = f"Obrigado {nome} pelo registro na nossa plataforma, agora você pode desfrutar dos nossos serviços."
    enviar_email(assunto, mensagem, destinatario)


def envia_email_quando_altera_usuario(nome, destinatario):
    assunto = "Alteração de usuário"
    mensagem = f"{nome} seus dados foram atualizados com sucesso."
    enviar_email(assunto, mensagem, destinatario)
