import flet as ft

def main(page: ft.Page):

    def on_register(e):
        # Ação do botão quando for clicado
        if name_input.value and email_input.value and password_input.value:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Cadastro realizado!"),
                content=ft.Text(f"Nome: {name_input.value}\nEmail: {email_input.value}")
            )
            page.dialog.open = True
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Todos os campos devem ser preenchidos!"))
            page.snack_bar.open = True
            page.update()

    # formulário
    name_input = ft.TextField(label="Nome", width=300)
    email_input = ft.TextField(label="Email", width=300)
    password_input = ft.TextField(label="Senha", password=True, width=300)
    
    # Botão de cadastro
    register_button = ft.ElevatedButton(text="Cadastrar", on_click=on_register)

    # elementos do layout da página
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Painel de Cadastro", # o nome "painel de cadastro" que aparece em cima dos campos
                    size=30, #tamanho das letras
                    weight=ft.FontWeight.BOLD, #peso da fonte
                    color=ft.colors.LIGHT_BLUE #cor do texto
                    ),
                    name_input,
                    email_input,
                    password_input,
                    register_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER, #centraliza
                horizontal_alignment=ft.CrossAxisAlignment.CENTER, #centraliza
            ),
            alignment=ft.alignment.center,  # centralizador do container das informações de cadastro
            width=page.window_width,  # largura com a das janela com as inf
            height=page.window_height,  # altura da janela das inf
            bgcolor=ft.colors.WHITE #isso define a cor de fundo
        )
    )

# Inicia a aplicação
ft.app(target=main)