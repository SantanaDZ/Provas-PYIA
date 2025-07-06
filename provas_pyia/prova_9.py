import flet as ft

def main(page: ft.Page):
    # Configurações da página
    page.title = "Lista de Tarefas"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Lista para armazenar as tarefas
    tarefas = []
    
    # Campo de entrada de texto
    campo_tarefa = ft.TextField(
        label="Digite uma nova tarefa",
        width=400,
        autofocus=True,
        on_submit=lambda e: adicionar_tarefa(e)
    )
    
    # Função para adicionar tarefa
    def adicionar_tarefa(e):
        if campo_tarefa.value:
            tarefas.append(campo_tarefa.value)
            campo_tarefa.value = ""
            atualizar_lista()
            campo_tarefa.focus()
    
    # Função para atualizar a lista exibida
    def atualizar_lista():
        # Limpa a lista atual
        lista_tarefas.controls.clear()
        
        # Adiciona cada tarefa à lista
        for tarefa in tarefas:
            lista_tarefas.controls.append(
                ft.ListTile(
                    title=ft.Text(tarefa),
                    leading=ft.Icon(ft.icons.TASK_ALT),
                )
            )
        # Adicione este código dentro da função main()

    # Função para remover tarefa
    def remover_tarefa(e):
        tarefas.remove(e.control.data)
        atualizar_lista()
    
    # Modifique a função atualizar_lista() para incluir botão de remover:
    def atualizar_lista():
        lista_tarefas.controls.clear()
        for tarefa in tarefas:
            lista_tarefas.controls.append(
                ft.ListTile(
                    title=ft.Text(tarefa),
                    leading=ft.Icon(ft.icons.TASK_ALT),
                    trailing=ft.IconButton(
                        icon=ft.icons.DELETE,
                        on_click=remover_tarefa,
                        data=tarefa
                    ),
                )
            )
        page.update()
        # Atualiza a página
        page.update()
    
    # Botão para adicionar tarefa
    botao_adicionar = ft.ElevatedButton(
        "Adicionar Tarefa",
        icon=ft.icons.ADD,
        on_click=adicionar_tarefa
    )
    
    # Lista para exibir as tarefas
    lista_tarefas = ft.ListView(expand=True)
    
    # Layout da aplicação
    page.add(
        ft.Column(
            [
                ft.Text("Lista de Tarefas", size=20, weight="bold"),
                ft.Row(
                    [
                        campo_tarefa,
                        botao_adicionar,
                    ],
                    alignment="center",
                ),
                ft.Divider(),
                lista_tarefas,
            ],
            spacing=20,
        )
    )

# Inicia o aplicativo
ft.app(target=main)