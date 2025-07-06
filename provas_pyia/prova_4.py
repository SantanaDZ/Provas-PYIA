# Função para calcular a média aritmética de três números
def media(num1, num2, num3):
    # Calculando a média aritmética
    resultado = (num1 + num2 + num3) / 3
    return resultado

# Exemplo de uso da função
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Chamando a função e exibindo o resultado
media_resultado = media(numero1, numero2, numero3)
print(f"A média aritmética dos números é: {media_resultado:.2f}")
