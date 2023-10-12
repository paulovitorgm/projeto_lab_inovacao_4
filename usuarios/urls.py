from django.urls import path
from usuarios.views import (cadastrar_usuario, editar_usuario,
                            alterar_senha, deleta_usuario, enviar_email)
from django.contrib.auth import views as views_auth

urlpatterns = [

    path('cadastro/', view=cadastrar_usuario, name='cadastrar_usuario'),
    path('editar/', view=editar_usuario, name='editar_usuario'),
    path('altera_senha/', view=alterar_senha, name='alterar_senha'),
    path('delete/<int:pk>/', view=deleta_usuario, name='deletar_usuario'),
    path('email/', view=enviar_email, name='enviar_email'),

    path('resetar_senha/', views_auth.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         name='resetar_senha'),

    path("resetar_senha/done/", views_auth.PasswordResetDoneView.as_view(template_name=
         'registration/password_reset_done.html'), name='resetar_senha-done'),

    path("resetar_senha/<uidb64>/<token>/", views_auth.PasswordResetConfirmView.as_view(template_name=
        'registration/password_reset_confirm.html'), name='resetar_senha-confirm'),

    path('resetar_senha/complete/', views_auth.PasswordResetCompleteView.as_view(template_name=
        'registration/password_reset_complete.html'), name='resetar_senha-complete'),

]
