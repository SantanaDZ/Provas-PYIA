import flet as ft
from datetime import datetime


class Pessoa:
    def __init__(self, nome, telefone, email):
        self._nome = nome
        self._telefone = telefone
        self._email = email
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def telefone(self):
        return self._telefone
    
    @property
    def email(self):
        return self._email
    
    def exibir_informacoes(self):
        return f"Nome: {self._nome}\nTelefone: {self._telefone}\nE-mail: {self._email}"


class Cliente(Pessoa):
    def __init__(self, nome, telefone, email, id_cliente):
        super().__init__(nome, telefone, email)
        self._id_cliente = id_cliente
    
    @property
    def id_cliente(self):
        return self._id_cliente
    
    def exibir_informacoes(self):
        info_base = super().exibir_informacoes()
        return f"{info_base}\nID Cliente: {self._id_cliente}"


class Quarto:
    def __init__(self, numero, tipo, preco_diaria):
        self._numero = numero
        self._tipo = tipo  # single, double, suite
        self._preco_diaria = preco_diaria
        self._disponivel = True
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def tipo(self):
        return self._tipo
    
    @property
    def preco_diaria(self):
        return self._preco_diaria
    
    @property
    def disponivel(self):
        return self._disponivel
    
    def reservar(self):
        if self._disponivel:
            self._disponivel = False
            return True
        return False
    
    def liberar(self):
        self._disponivel = True
    
    def exibir_info(self):
        status = "Disponível" if self._disponivel else "Ocupado"
        return f"Quarto {self._numero} - {self._tipo.capitalize()} - R${self._preco_diaria:.2f}/noite - {status}"


class Reserva:
    def __init__(self, cliente, quarto, data_checkin, data_checkout):
        self._cliente = cliente
        self._quarto = quarto
        self._data_checkin = data_checkin
        self._data_checkout = data_checkout
        self._ativa = True
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def quarto(self):
        return self._quarto
    
    @property
    def data_checkin(self):
        return self._data_checkin
    
    @property
    def data_checkout(self):
        return self._data_checkout
    
    @property
    def ativa(self):
        return self._ativa
    
    def cancelar(self):
        if self._ativa:
            self._quarto.liberar()
            self._ativa = False
            return True
        return False
    
    def exibir_info(self):
        status = "Ativa" if self._ativa else "Cancelada"
        return f"Reserva para {self._cliente.nome}\nQuarto: {self._quarto.numero}\nCheck-in: {self._data_checkin}\nCheck-out: {self._data_checkout}\nStatus: {status}"


class GerenciadorDeReservas:
    def __init__(self):
        self._clientes = []
        self._quartos = []
        self._reservas = []
    
    def adicionar_cliente(self, cliente):
        self._clientes.append(cliente)
    
    def adicionar_quarto(self, quarto):
        self._quartos.append(quarto)
    
    def buscar_cliente_por_id(self, id_cliente):
        for cliente in self._clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None
    
    def buscar_quarto_por_numero(self, numero_quarto):
        for quarto in self._quartos:
            if quarto.numero == numero_quarto:
                return quarto
        return None
    
    def quartos_disponiveis(self):
        return [quarto for quarto in self._quartos if quarto.disponivel]
    
    def criar_reserva(self, id_cliente, numero_quarto, data_checkin, data_checkout):
        cliente = self.buscar_cliente_por_id(id_cliente)
        quarto = self.buscar_quarto_por_numero(numero_quarto)
        
        if not cliente or not quarto:
            return False
        
        if not quarto.disponivel:
            return False
        
        if quarto.reservar():
            reserva = Reserva(cliente, quarto, data_checkin, data_checkout)
            self._reservas.append(reserva)
            return True
        return False
    
    def cancelar_reserva(self, id_cliente, numero_quarto):
        for reserva in self._reservas:
            if (reserva.cliente.id_cliente == id_cliente and 
                reserva.quarto.numero == numero_quarto and 
                reserva.ativa):
                return reserva.cancelar()
        return False
    
    def listar_reservas(self):
        return [reserva.exibir_info() for reserva in self._reservas if reserva.ativa]
    
    def listar_clientes(self):
        return [cliente.exibir_informacoes() for cliente in self._clientes]
    
    def listar_quartos(self):
        return [quarto.exibir_info() for quarto in self._quartos]

def main(page: ft.Page):
    page.title = "Refúgio dos Sonhos - Sistema de Reservas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Inicializar gerenciador
    gerenciador = GerenciadorDeReservas()
    
    # Adicionar alguns dados de exemplo
    gerenciador.adicionar_cliente(Cliente("João Silva", "11987654321", "joao@email.com", "CL001"))
    gerenciador.adicionar_cliente(Cliente("Maria Souza", "21987654321", "maria@email.com", "CL002"))
    
    gerenciador.adicionar_quarto(Quarto(101, "single", 250.00))
    gerenciador.adicionar_quarto(Quarto(201, "double", 350.00))
    gerenciador.adicionar_quarto(Quarto(301, "suite", 500.00))
    
    # Elementos da interface
    titulo = ft.Text("Refúgio dos Sonhos - Sistema de Reservas", size=24, weight=ft.FontWeight.BOLD)
    
    # Tabs para navegação
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Quartos"),
            ft.Tab(text="Clientes"),
            ft.Tab(text="Reservas"),
            ft.Tab(text="Nova Reserva"),
        ],
        expand=1,
    )
    
    # Conteúdo das tabs
    conteudo_quartos = ft.Column()
    conteudo_clientes = ft.Column()
    conteudo_reservas = ft.Column()
    conteudo_nova_reserva = ft.Column()
    
    def atualizar_quartos():
        conteudo_quartos.controls.clear()
        for quarto in gerenciador.listar_quartos():
            conteudo_quartos.controls.append(
                ft.Text(quarto, size=16))
        page.update()
    
    def atualizar_clientes():
        conteudo_clientes.controls.clear()
        for cliente in gerenciador.listar_clientes():
            conteudo_clientes.controls.append(
                ft.Text(cliente, size=16))
        page.update()
    
    def atualizar_reservas():
        conteudo_reservas.controls.clear()
        for reserva in gerenciador.listar_reservas():
            conteudo_reservas.controls.append(
                ft.Text(reserva, size=16))
        page.update()
    
    def criar_nova_reserva(e):
        id_cliente = dropdown_clientes.value
        numero_quarto = int(dropdown_quartos.value)
        data_checkin = checkin_picker.value
        data_checkout = checkout_picker.value
        
        if not all([id_cliente, numero_quarto, data_checkin, data_checkout]):
            mensagem_nova_reserva.value = "Preencha todos os campos!"
            page.update()
            return
        
        if gerenciador.criar_reserva(id_cliente, numero_quarto, data_checkin, data_checkout):
            mensagem_nova_reserva.value = "Reserva criada com sucesso!"
            atualizar_quartos()
            atualizar_reservas()
        else:
            mensagem_nova_reserva.value = "Erro ao criar reserva. Verifique os dados."
        page.update()
    
    # Componentes para nova reserva
    dropdown_clientes = ft.Dropdown(
        label="Cliente",
        options=[]
    )
    
    dropdown_quartos = ft.Dropdown(
        label="Quarto",
        options=[]
    )
    
    checkin_picker = ft.TextField(
        label="Data de Check-in (DD/MM/AAAA)",
        hint_text="01/01/2023"
    )
    
    checkout_picker = ft.TextField(
        label="Data de Check-out (DD/MM/AAAA)",
        hint_text="05/01/2023"
    )
    
    botao_reservar = ft.ElevatedButton(
        text="Confirmar Reserva",
        on_click=criar_nova_reserva
    )
    
    mensagem_nova_reserva = ft.Text()
    
    # Preencher dropdowns
    def preencher_dropdowns():
        dropdown_clientes.options.clear()
        for cliente in gerenciador._clientes:
            dropdown_clientes.options.append(
                ft.dropdown.Option(cliente.id_cliente, f"{cliente.nome} ({cliente.id_cliente})"))
        
        dropdown_quartos.options.clear()
        for quarto in gerenciador.quartos_disponiveis():
            dropdown_quartos.options.append(
                ft.dropdown.Option(str(quarto.numero), f"Quarto {quarto.numero} - {quarto.tipo}"))
        
        page.update()
    
    # Configurar conteúdo das tabs
    def change_tab(e):
        if tabs.selected_index == 0:
            atualizar_quartos()
            conteudo_tab.content = conteudo_quartos
        elif tabs.selected_index == 1:
            atualizar_clientes()
            conteudo_tab.content = conteudo_clientes
        elif tabs.selected_index == 2:
            atualizar_reservas()
            conteudo_tab.content = conteudo_reservas
        elif tabs.selected_index == 3:
            preencher_dropdowns()
            conteudo_nova_reserva.controls = [
                dropdown_clientes,
                dropdown_quartos,
                checkin_picker,
                checkout_picker,
                botao_reservar,
                mensagem_nova_reserva
            ]
            conteudo_tab.content = conteudo_nova_reserva
        page.update()
    
    tabs.on_change = change_tab
    
    conteudo_tab = ft.Container()
    change_tab(None)  # Inicializar com a primeira tab
    
    # Layout principal
    page.add(
        ft.Column(
            [
                titulo,
                tabs,
                conteudo_tab
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        )
    )

ft.app(target=main)