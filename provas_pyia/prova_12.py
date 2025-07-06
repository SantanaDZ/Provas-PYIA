class Veiculo:
    def movimentar(self):
        print("Veículo está em movimento.")


class Carro(Veiculo):
    def movimentar(self):
        print("Carro está dirigindo.")


class Moto(Veiculo):
    def movimentar(self):
        print("Moto está acelerando.")


# Testando as classes
veiculo = Veiculo()
carro = Carro()
moto = Moto()

# Chamando o método movimentar de cada objeto
veiculo.movimentar()  # Saída: Veículo está em movimento.
carro.movimentar()    # Saída: Carro está dirigindo.
moto.movimentar()     # Saída: Moto está acelerando.