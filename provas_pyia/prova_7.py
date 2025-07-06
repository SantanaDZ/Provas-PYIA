import random

def lancar_dados():
    """Simula o lançamento de dois dados e retorna a soma dos resultados.
    
    Returns:
        int: Soma dos valores dos dois dados (entre 2 e 12)
    """
    dado1 = random.randint(1, 6)  # Lança o primeiro dado (valor entre 1 e 6)
    dado2 = random.randint(1, 6)  # Lança o segundo dado (valor entre 1 e 6)
    return dado1 + dado2  # Retorna a soma dos dois dados

resultado = lancar_dados()
print(f"O resultado do lançamento dos dados foi: {resultado}")