def adicionar_tarefa(lista_de_tarefas, tarefa):
    """Adiciona nova tarefa a uma lisat pré-existente"""
    lista_de_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
    """Exibe a lista de tarefas numerada"""
    print('\n'+"*" * 50)
    print(f"{' ' * 17}Lista de Tarefas")
    print("-" * 50)
    n = 1
    for tarefa in lista_de_tarefas:
        print(f"{n} - {tarefa}") # f string
        n += 1
    if len(lista_de_tarefas) == 0:
        print(f"{" " * 18}*** VAZIA ***")
    print("-" * 50)

def remover_tarefa(lista_de_tarefas, tarefa):
    """Remove uma tarefa pré-existente da lista a partir do número dela"""
    lista_de_tarefas.pop(tarefa - 1) #subtrai 1 para que o valor referencia do usuario seja igual ao valor da lista
    return lista_de_tarefas

def exibir_menu():
    """Exibe menu com astarefas numeradas para o usuário escolher"""
    print("Escolha uma opção:\n" \
        "1 - Inserir nova tarefa\n" \
        "2 - Listar tarefas\n" \
        "3 - Remover tarefa\n" \
        "4 - Sair"
    )
# Inicialização de variáveis
lista_de_tarefas = []
continuar = True

# Cabeçalho do programa
print("\nBem-vinde à sua Lista de Tarefas!")
print("-" * 50)
print('\n')

# Loop principal
while continuar:
    exibir_menu()
    opcao = input("Insira o que deseja fazer: ").lower()

    if opcao == "1":
        tarefa = input('Insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
    elif opcao == "2":
        listar_tarefas(lista_de_tarefas)
    elif opcao == "3":
        # A condicional verifica se o valor é numero, se é, converte o numero_istring em numero_int e verifica se é maior que a lista e menor ou igual a 0 
        tarefa = input('Insira o número da tarefa que deseja remover: ')
        if tarefa.isnumeric() == False:
            print("Número inválido! Tente novamente.")
        elif int(tarefa) > len(lista_de_tarefas) or int(tarefa) <= 0:    
            print("Número inválido! Tente novamente.")
        else:
            remover_tarefa(lista_de_tarefas, int(tarefa))
            print("Tarefa removida!")
    elif opcao == "4" or opcao == "sair":
        continuar = False
    else:
        print("Opção inválida! Por favor, tente novamente." )
    print('\n')