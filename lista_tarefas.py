#Projeto: lista_tarefas Aluna: Karina Nerone
tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    if tarefa.strip():
        tarefas.append(tarefa)
        print("Tarefa adicionada.")
    else:
        print("Tarefas vazias não são permitidas.")

def ver_tarefas():
    if tarefas:
        print("Suas tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa para exibir.")

def main():
    while True:
        print("\nLista de Tarefas")
        print("-----------------")
        print("1. Adicionar tarefa")
        print("2. Ver tarefas")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_tarefa()
        elif escolha == "2":
            ver_tarefas()
        elif escolha == "3":
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()