class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        # Atributos privados para saldo e titular
        self._titular = titular
        self._saldo = saldo_inicial
    
    # Método para depositar um valor na conta
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print("Valor de depósito inválido!")
    
    # Método para sacar um valor da conta
    def sacar(self, valor):
        if valor > 0:
            if valor <= self._saldo:
                self._saldo -= valor
                print(f"Saque de R${valor} realizado com sucesso!")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque inválido!")
    
    # Método para exibir o saldo atual da conta
    def exibir_saldo(self):
        print(f"Saldo atual da conta de {self._titular}: R${self._saldo}")
    
    # Método para acessar o titular da conta (getter)
    def get_titular(self):
        return self._titular
    
    # Método para acessar o saldo (getter)
    def get_saldo(self):
        return self._saldo

# Exemplo de uso da classe ContaBancaria
if __name__ == "__main__":
    # Criando uma conta bancária
    conta = ContaBancaria("João Silva", 500)

    # Exibindo o saldo inicial
    conta.exibir_saldo()

    # Depositando dinheiro na conta
    conta.depositar(200)

    # Tentando sacar mais do que o saldo disponível
    conta.sacar(800)

    # Sacando um valor válido
    conta.sacar(300)

    # Exibindo o saldo após as transações
    conta.exibir_saldo()
