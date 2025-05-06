import json

def put_id():
    try:
        with open('tarefas.json', 'r') as idd:
            task = json.load(idd)
            size = len(task)
            obj = task[size - 1]

            id = obj['id'] + 1

            return id
            
    except Exception as e:
        print(f"Erro ao pegar id {e}")

def listarTarefas(task):
    # Função responsável por organizar as informações lidas do arquivo json.

    size = len(task)

    objectt = {'Tarefas':[], 
               'Concluida':[]}
    
    for x in task:
        objectt['Tarefas'].append(x['titulo'])
        objectt['Concluida'].append(x['concluida'])
    
    result = lambda x: "feita" if x == True else "A fazer"

    print("")
    for i in range(0, size):
        print(f"{i + 1}  Tarefa: {objectt['Tarefas'][i]}: Estado: {result(objectt['Concluida'][i])}")
    
    print(f"\n -- Número de tarefas na lista {size} --\n")
    