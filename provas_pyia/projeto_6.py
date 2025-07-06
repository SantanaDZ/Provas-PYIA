import sys
from typing import Dict, List, Set, TypedDict

class Tarefa(TypedDict):
    nome: str
    descricao: str
    prioridade: str
    categoria: str
    concluida: bool

# Estrutura de dados para armazenar tarefas
tarefas: List[Tarefa] = []
categorias_disponiveis: Set[str] = set()
prioridades_validas = {"alta", "media", "baixa"}

def adicionar_tarefa(nome: str, descricao: str, prioridade: str, categoria: str) -> None:
    """Adiciona uma nova tarefa à lista."""
    if prioridade.lower() not in prioridades_validas:
        print(f"Prioridade inválida. Use uma destas: {', '.join(prioridades_validas)}")
        return
    
    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade.lower(),
        "categoria": categoria.lower(),
        "concluida": False
    }
    
    tarefas.append(tarefa)
    categorias_disponiveis.add(categoria.lower())
    print(f"Tarefa '{nome}' adicionada com sucesso!")

def listar_tarefas(filtro_prioridade: str = None, filtro_categoria: str = None) -> None:
    """Lista todas as tarefas, com opção de filtrar por prioridade ou categoria."""
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    print("\nLista de Tarefas:")
    print("-" * 40)
    
    for idx, tarefa in enumerate(tarefas, 1):
        if filtro_prioridade and tarefa["prioridade"] != filtro_prioridade.lower():
            continue
        if filtro_categoria and tarefa["categoria"] != filtro_categoria.lower():
            continue
            
        status = "✓" if tarefa["concluida"] else " "
        print(f"{idx}. [{status}] {tarefa['nome']}")
        print(f"   Descrição: {tarefa['descricao']}")
        print(f"   Prioridade: {tarefa['prioridade'].capitalize()}")
        print(f"   Categoria: {tarefa['categoria'].capitalize()}")
        print("-" * 40)

def marcar_como_concluida(indice: int) -> None:
    """Marca uma tarefa como concluída."""
    try:
        if tarefas[indice - 1]["concluida"]:
            print("Esta tarefa já está marcada como concluída.")
        else:
            tarefas[indice - 1]["concluida"] = True
            print(f"Tarefa '{tarefas[indice - 1]['nome']}' marcada como concluída!")
    except IndexError:
        print("Índice inválido. Use o número da tarefa conforme listado.")

def remover_tarefa(indice: int) -> None:
    """Remove uma tarefa da lista."""
    try:
        nome = tarefas[indice - 1]["nome"]
        del tarefas[indice - 1]
        print(f"Tarefa '{nome}' removida com sucesso!")
    except IndexError:
        print("Índice inválido. Use o número da tarefa conforme listado.")

def mostrar_categorias() -> None:
    """Mostra todas as categorias disponíveis."""
    if not categorias_disponiveis:
        print("Nenhuma categoria cadastrada ainda.")
        return
    
    print("\nCategorias disponíveis:")
    for idx, categoria in enumerate(sorted(categorias_disponiveis), 1):
        print(f"{idx}. {categoria.capitalize()}")

def mostrar_estatisticas() -> None:
    """Mostra estatísticas sobre as tarefas."""
    total = len(tarefas)
    concluidas = sum(1 for t in tarefas if t["concluida"])
    
    print("\nEstatísticas:")
    print(f"Total de tarefas: {total}")
    print(f"Tarefas concluídas: {concluidas} ({concluidas/total*100:.1f}%)" if total else "0")
    print(f"Tarefas pendentes: {total - concluidas}")
    
    print("\nTarefas por prioridade:")
    for prioridade in prioridades_validas:
        count = sum(1 for t in tarefas if t["prioridade"] == prioridade)
        print(f"{prioridade.capitalize()}: {count}")

def menu() -> None:
    """Exibe o menu de opções."""
    print("\n" + "=" * 40)
    print("Gerenciador de Tarefas Diárias".center(40))
    print("=" * 40)
    print("1. Adicionar nova tarefa")
    print("2. Listar todas as tarefas")
    print("3. Listar tarefas por prioridade")
    print("4. Listar tarefas por categoria")
    print("5. Marcar tarefa como concluída")
    print("6. Remover tarefa")
    print("7. Mostrar categorias disponíveis")
    print("8. Mostrar estatísticas")
    print("9. Sair")
    print("=" * 40)

def main() -> None:
    """Função principal do programa."""
    print("Bem-vindo ao Gerenciador de Tarefas Diárias!")
    
    while True:
        menu()
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            print("\nAdicionar Nova Tarefa")
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição: ")
            prioridade = input("Prioridade (alta/media/baixa): ")
            categoria = input("Categoria: ")
            adicionar_tarefa(nome, descricao, prioridade, categoria)
        
        elif opcao == "2":
            listar_tarefas()
        
        elif opcao == "3":
            prioridade = input("Digite a prioridade para filtrar (alta/media/baixa): ")
            if prioridade.lower() in prioridades_validas:
                listar_tarefas(filtro_prioridade=prioridade)
            else:
                print("Prioridade inválida.")
        
        elif opcao == "4":
            categoria = input("Digite a categoria para filtrar: ")
            listar_tarefas(filtro_categoria=categoria)
        
        elif opcao == "5":
            listar_tarefas()
            if tarefas:
                try:
                    indice = int(input("Digite o número da tarefa a marcar como concluída: "))
                    marcar_como_concluida(indice)
                except ValueError:
                    print("Por favor, digite um número válido.")
        
        elif opcao == "6":
            listar_tarefas()
            if tarefas:
                try:
                    indice = int(input("Digite o número da tarefa a remover: "))
                    remover_tarefa(indice)
                except ValueError:
                    print("Por favor, digite um número válido.")
        
        elif opcao == "7":
            mostrar_categorias()
        
        elif opcao == "8":
            mostrar_estatisticas()
        
        elif opcao == "9":
            print("Obrigado por usar o Gerenciador de Tarefas. Até logo!")
            sys.exit(0)
        
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 9.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()