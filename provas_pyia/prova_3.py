# Criando um dicionário vazio para armazenar os produtos e seus preços
produtos = {}

# Solicitando os dados dos produtos
for i in range(5):
    nome_produto = input(f"Digite o nome do produto {i+1}: ")
    preco_produto = float(input(f"Digite o preço do produto {nome_produto}: R$ "))
    
    # Armazenando o nome do produto como chave e o preço como valor
    produtos[nome_produto] = preco_produto

# Calculando o valor total da compra
valor_total = sum(produtos.values())

# Exibindo o dicionário com os produtos e preços
print("\nProdutos e preços cadastrados:")
for nome, preco in produtos.items():
    print(f"{nome}: R$ {preco:.2f}")

# Exibindo o valor total da compra
print(f"\nValor total da compra: R$ {valor_total:.2f}")
