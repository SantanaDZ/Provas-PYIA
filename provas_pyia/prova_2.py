# Coletando dados do usuário
nome = input("Digite o nome do contato: ")
telefone = input("Digite o número de telefone do contato: ")
email = input("Digite o endereço de email do contato: ")

# Criando o dicionário
contato = {
    "nome": nome,
    "telefone": telefone,
    "email": email
}

# Exibindo o dicionário com as informações do contato
print("\nInformações do contato:")
for chave, valor in contato.items():
    print(f"{chave.capitalize()}: {valor}")