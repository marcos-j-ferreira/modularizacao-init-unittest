from tarefas import add_task, mark, readJson
import os

def main():
    # Função responsável por gerenciar todas as outras funções, como chamar e passar parâmetros.

    ope = " -- To-do --\n Escolha uma opção\n 1 - adicionar\n 2 - Listar tarefas\n 3 - Marcar como concluida\n 4 - Encerrar o programa"

    n = 0

    while n < 4:

        print(ope)
        chose = int(input())

        if chose == 1:
            os.system("cls")
            print("Escreva a tarefa que deseja adicionar: ")
            tarefa = str(input())
            add_task(tarefa)

        elif chose == 2:
            os.system("cls")
            readJson()

        elif chose == 3:
            os.system("cls")
            #print("Digite o número da tarefa que deseja marcar como conluida: ")
            readJson()
            id = int(input("Escolha o número da tarefa que deseja concluir: "))
            mark(id)

        elif chose == 4:
            n = 5
            print("Fim do programa")
        else:
            print("Digite um número valido")

if __name__ == "__main__":
    main()