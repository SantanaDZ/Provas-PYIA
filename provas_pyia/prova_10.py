import flet as ft
import re  # Para validação de e-mail

def main(page: ft.Page):
    # Configurações de tema
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.INDIGO,
            secondary=ft.colors.PINK,
        ),
    )
    
    # Configurações da página
    page.title = "Formulário de Contato"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30
    
    # Elementos do formulário
    nome = ft.TextField(
        label="Nome completo",
        width=400,
        autofocus=True,
        border_color=ft.colors.INDIGO
    )
    
    email = ft.TextField(
        label="E-mail", 
        width=400,
        border_color=ft.colors.INDIGO
    )
    
    mensagem = ft.TextField(
        label="Mensagem", 
        width=400, 
        multiline=True, 
        min_lines=4,
        max_lines=6,
        border_color=ft.colors.INDIGO
    )
    
    # Área para mensagem de confirmação
    confirmacao = ft.Column(visible=False)
    
    def enviar_formulario(e):
        # Resetar erros
        nome.error_text = ""
        email.error_text = ""
        mensagem.error_text = ""
        
        # Validação dos campos
        if not nome.value:
            nome.error_text = "Por favor, digite seu nome"
            page.update()
            return
            
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email.value):
            email.error_text = "Por favor, digite um e-mail válido"
            page.update()
            return
            
        if not mensagem.value or len(mensagem.value) < 10:
            mensagem.error_text = "Por favor, digite uma mensagem com pelo menos 10 caracteres"
            page.update()
            return
            
        # Processamento dos dados
        dados = {
            "nome": nome.value,
            "email": email.value,
            "mensagem": mensagem.value
        }
        
        # Salvar em arquivo
        with open("contatos.txt", "a", encoding="utf-8") as f:
            f.write(f"Nome: {dados['nome']}\nE-mail: {dados['email']}\nMensagem: {dados['mensagem']}\n{'='*30}\n")
        
        # Mostra mensagem de confirmação
        confirmacao.controls = [
            ft.Icon(ft.icons.CHECK_CIRCLE, color=ft.colors.GREEN, size=40),
            ft.Text("Formulário enviado com sucesso!", size=20, weight="bold"),
            ft.Text(f"Obrigado {nome.value}, entraremos em contato em breve!"),
        ]
        confirmacao.visible = True
        
        # Limpa o formulário
        nome.value = ""
        email.value = ""
        mensagem.value = ""
        
        page.update()
    
    # Botão de envio
    botao_enviar = ft.ElevatedButton(
        "Enviar Mensagem",
        icon=ft.icons.SEND,
        on_click=enviar_formulario,
        width=400,
        height=50,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.INDIGO,
            color=ft.colors.WHITE,
        )
    )
    
    # Layout do aplicativo
    page.add(
        ft.Column(
            [
                ft.Text("Formulário de Contato", size=24, weight="bold", color=ft.colors.INDIGO),
                ft.Divider(height=10, color=ft.colors.PINK),
                nome,
                email,
                mensagem,
                botao_enviar,
                ft.Divider(height=10, color=ft.colors.PINK),
                confirmacao
            ],
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)