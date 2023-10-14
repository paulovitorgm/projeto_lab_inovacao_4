from django.contrib.auth.models import User
from django.core.mail import send_mail, send_mass_mail
from django.db.models.signals import post_save

from usuarios.models import Usuario
from ProjetoJogos.settings import DEFAULT_FROM_EMAIL


def email_confirmacao_de_cadastro(sender, instance, created, **kwargs):
    if created:
        envia_email_quando_cria_usuario(instance.first_name, instance.email)
    else:
        envia_email_quando_altera_usuario(instance.first_name, instance.email)


def email_avisando_alteracao_de_cadastro(sender, instance, created, **kwargs):
    if not created:
        usuario = User.objects.filter(usuario=instance).first()
        envia_email_quando_altera_usuario(usuario.first_name, usuario.email)


post_save.connect(email_confirmacao_de_cadastro, sender=User)

post_save.connect(email_avisando_alteracao_de_cadastro, sender=Usuario)


def enviar_email(assunto, mensagem, destinatario):
    send_mail(assunto, mensagem, DEFAULT_FROM_EMAIL, recipient_list=[destinatario])


def envia_email_quando_cria_usuario(nome, destinatario):
    assunto = "Criação de conta"
    mensagem = f"Obrigado {nome} pelo registro na nossa plataforma, agora você pode desfrutar dos nossos serviços."
    enviar_email(assunto, mensagem, destinatario)


def envia_email_quando_altera_usuario(nome, destinatario):
    assunto = "Alteração de usuário"
    mensagem = f"{nome} seus dados foram atualizados com sucesso."
    enviar_email(assunto, mensagem, destinatario)
