from utils import put_id, listarTarefas
import json

# Pode listar, adicionar e marcar como concluídas

def readJson():
    # Essa função irá ler o arquivo json, e organizar os dados para serem exibidos para o usuário.

    with open('tarefas.json', 'r') as arquivo:
        task = json.load(arquivo)
        listarTarefas(task)

def add_task(tarefa):
    # Essa função adiciona uma nova tarefa na lista de tarefas.

    with open('tarefas.json', 'r') as idd:
        task = json.load(idd)
        size = len(task)
        obj = task[size - 1]
    
    id = put_id()

    model =     {
        'id': id,
        'titulo': tarefa,
        'concluida':False
    }

    with open('tarefas.json', 'r') as arquivo:
        tarefas = json.load(arquivo)

        tarefas.append(model)

    with open('tarefas.json', 'w') as file:
        json.dump(tarefas, file, indent=4)
    
    return print("-- Tarefa adicionada com sucesso --\n")

def mark(id):
    # Função responsável por marcar o estado de uma tarefa

    try:
        with open ('tarefas.json', 'r') as file:
            db = json.load(file)
            size = 0
            for i in db:
                if id == i['id']:
                    db[size]['concluida'] = True
                size += 1
        
        with open('tarefas.json', 'w')as arquivo:
            json.dump(db, arquivo, indent=4)

            return print("Tarefa marcada como conluida com sucesso")
        
    except Exception as e:
        print(f"Erro ao pegar id:{id}")