def adicionar_tarefa(lista_de_tarefas, tarefa):
    lista_de_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
    print('\n'+"*" * 50)
    print("Lista de Tarefas")
    print("-" * 50)
    for tarefa in lista_de_tarefas:
        print(f"* {tarefa}") # f string
    print("-" * 50)

def exibir_menu():
    print("Escolha uma opção:\n" \
        "1 - Inserir nova tarefa\n" \
        "2 - Listar tarefas \n" \
        "3 - Sair"
    )

lista_de_tarefas = []
continuar = True

while continuar:
    exibir_menu()
    opcao = input("Insira o que deseja fazer: ").lower()

    if opcao == "1":
        tarefa = input('Insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
    elif opcao == "2":
        listar_tarefas(lista_de_tarefas)
    elif opcao == "3" or opcao == "sair":
        continuar = False
    else:
        print("Opção inválida! Por favor, tente novamente." )
    print('\n')