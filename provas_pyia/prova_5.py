# Função para encontrar o maior número entre três
def maior_numero(num1, num2, num3):
    # Comparando os números para identificar o maior
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Exemplo de uso da função
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Chamando a função e exibindo o resultado
maior = maior_numero(numero1, numero2, numero3)
print(f"O maior número entre os três é: {maior}")
