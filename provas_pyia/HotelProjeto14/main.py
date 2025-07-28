import flet as ft
import db
from datetime import datetime

def main(page: ft.Page):
    page.title = "Painel de Reservas - Hotel Refúgio"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    titulo = ft.Text("Refúgio dos Sonhos - Painel Administrativo", size=26, weight=ft.FontWeight.BOLD)

    aba_clientes = ft.Column()
    aba_quartos = ft.Column()
    aba_reservas = ft.Column()

    def atualizar_clientes():
        aba_clientes.controls.clear()
        for c in db.obter_clientes():
            aba_clientes.controls.append(
                ft.Card(
                    content=ft.ListTile(
                        title=ft.Text(c["nome"], weight="bold"),
                        subtitle=ft.Text(f"ID: {c['id_cliente']}\nTelefone: {c['telefone']}\nEmail: {c['email']}"),
                        trailing=ft.IconButton(icon=ft.Icons.DELETE, icon_color="red", on_click=lambda e, id=c['id_cliente']: (db.deletar_cliente(id), atualizar_clientes()))
                    ),
                    elevation=1, margin=10
                )
            )
        page.update()

    def atualizar_quartos():
        aba_quartos.controls.clear()
        for q in db.obter_quartos():
            cor = "green" if q["disponivel"] else "red"
            status = "Disponível" if q["disponivel"] else "Ocupado"
            aba_quartos.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.ListTile(
                            title=ft.Text(f"Quarto {q['numero']} - {q['tipo'].title()}", weight="bold"),
                            subtitle=ft.Text(f"Preço: R${q['preco_diaria']} - {status}"),
                            trailing=ft.IconButton(icon=ft.Icons.DELETE, icon_color="red", on_click=lambda e, num=q['numero']: (db.deletar_quarto(num), atualizar_quartos()))
                        ),
                        bgcolor=f"{cor}10",  # Define cor de fundo aqui no container
                        padding=10,
                        border_radius=5,
                    ),
                    elevation=1,
                    margin=10
                )
            )
        page.update()


    def atualizar_reservas():
        aba_reservas.controls.clear()
        for r in db.obter_reservas():
            aba_reservas.controls.append(
                ft.Card(
                    content=ft.ListTile(
                        title=ft.Text(f"Reserva de {r['nome_cliente']}", weight="bold"),
                        subtitle=ft.Text(f"Check-in: {r['checkin']} - Check-out: {r['checkout']}\nQuarto: {r['numero_quarto']} - {r['tipo']}"),
                        trailing=ft.IconButton(icon=ft.Icons.CANCEL, icon_color="red", tooltip="Cancelar", on_click=lambda e, rid=r['id']: (db.cancelar_reserva(rid), atualizar_reservas(), atualizar_quartos()))
                    ),
                    elevation=1, margin=10
                )
            )
        page.update()

    # Formulários de cadastro
    # id_input = ft.TextField(label="ID Cliente")
    nome_input = ft.TextField(label="Nome")
    telefone_input = ft.TextField(label="Telefone")
    email_input = ft.TextField(label="Email")
    btn_add_cliente = ft.ElevatedButton("Adicionar Cliente", on_click=lambda e: (
    db.adicionar_cliente(nome_input.value, telefone_input.value, email_input.value),
    atualizar_clientes()
))

    numero_quarto = ft.TextField(label="Número")
    tipo_quarto = ft.TextField(label="Tipo (single/double/suite)")
    preco_quarto = ft.TextField(label="Preço diária")
    btn_add_quarto = ft.ElevatedButton("Adicionar Quarto", on_click=lambda e: (db.adicionar_quarto(int(numero_quarto.value), tipo_quarto.value, float(preco_quarto.value)), atualizar_quartos()))

    reserva_cliente = ft.TextField(label="ID do Cliente")
    reserva_quarto = ft.TextField(label="Número do Quarto")
    reserva_checkin = ft.TextField(label="Check-in (AAAA-MM-DD)")
    reserva_checkout = ft.TextField(label="Check-out (AAAA-MM-DD)")
    btn_add_reserva = ft.ElevatedButton("Reservar", on_click=lambda e: (db.criar_reserva(reserva_cliente.value, int(reserva_quarto.value), reserva_checkin.value, reserva_checkout.value), atualizar_reservas(), atualizar_quartos()))

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Clientes", icon=ft.Icons.PEOPLE),
            ft.Tab(text="Quartos", icon=ft.Icons.HOTEL),
            ft.Tab(text="Reservas", icon=ft.Icons.CALENDAR_MONTH)
        ]
    )

    conteudo = ft.Container(content=aba_clientes)

    def trocar_aba(e):
        match tabs.selected_index:
            case 0:
                conteudo.content = ft.Column([
                    ft.Text("Cadastro de Clientes", size=18, weight="bold"),
                    nome_input, telefone_input, email_input, btn_add_cliente,
                    ft.Divider(),
                    ft.Text("Lista de Clientes", size=18, weight="bold"),
                    aba_clientes
                ])
                atualizar_clientes()
            case 1:
                conteudo.content = ft.Column([
                    ft.Text("Cadastro de Quartos", size=18, weight="bold"),
                    numero_quarto, tipo_quarto, preco_quarto, btn_add_quarto,
                    ft.Divider(),
                    ft.Text("Lista de Quartos", size=18, weight="bold"),
                    aba_quartos
                ])
                atualizar_quartos()
            case 2:
                conteudo.content = ft.Column([
                    ft.Text("Nova Reserva", size=18, weight="bold"),
                    reserva_cliente, reserva_quarto, reserva_checkin, reserva_checkout, btn_add_reserva,
                    ft.Divider(),
                    ft.Text("Reservas Ativas", size=18, weight="bold"),
                    aba_reservas
                ])
                atualizar_reservas()
        page.update()

    tabs.on_change = trocar_aba
    trocar_aba(None)

    page.add(
        ft.Column([
            titulo,
            tabs,
            conteudo
        ])
    )

ft.app(target=main)
