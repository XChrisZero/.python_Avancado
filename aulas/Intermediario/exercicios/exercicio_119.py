import json
# Exercício - Lista de tarefas com desfazer e refazer

# Funções para manipular a lista de tarefas
def listar(tarefas):
    print (  )
    if not tarefas: # Verifica se a lista está vazia
        print ( 'Nenhuma tarefa para listar' )
        return  
     
    print ('Tarefas:')
    for tarefa in tarefas: # Itera e imprime cada tarefa
        print ( f'\t{tarefa}' )
    print (  )

# Função para desfazer a última tarefa
def desfazer(tarefas, tarefas_refazer): 
    print (  )
    if not tarefas: # Verifica se a lista está vazia
        print ( 'Nenhuma tarefa para desfazer' )
        return
    
    tarefa = tarefas.pop() # Remove a última tarefa da lista
    print ( f'{tarefa=} removida da lista.' )
    tarefas_refazer.append(tarefa) # Adiciona a tarefa removida na lista de refazer
    print (  )
    listar(tarefas)
 
# Função para refazer a última tarefa desfeita
def refazer(tarefas, tarefas_refazer):
    print (  )
    if not tarefas_refazer: # Verifica se a lista de refazer está vazia
        print ( 'Nenhuma tarefa para refazer' )
        return
    
    tarefa = tarefas_refazer.pop() # Remove a última tarefa da lista de refazer
    print ( f'{tarefa=} readicionada na lista.' )
    tarefas.append(tarefa) # Adiciona a tarefa removida na lista de tarefas
    print (  )
    listar(tarefas)

# Função para adicionar uma nova tarefa
def adicionar(tarefa, tarefas):
    print (  )
    tarefa = tarefa.strip()
    if not tarefa: # Verifica se a tarefa está vazia
        print ( 'não tem tarefas a fazer!' )
        return
    print ( f'{tarefa=} adicionada na lista.' )
    
    tarefas.append(tarefa) # Adiciona a tarefa na lista de tarefas
    print (  )
    listar(tarefas)

# Função para salvar as tarefas em um arquivo JSON
def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados

# Função para salvar as tarefas em um arquivo JSON
def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados

#função para sair
def sair():
    print('Saindo...')
    exit()


# Caminho do arquivo JSON para salvar as tarefas
CAMINHO_ARQUIVO = 'exercicio_119.json'

# Listas para armazenar as tarefas e as tarefas desfeitas
tarefas = ler([], CAMINHO_ARQUIVO)

# Lista para armazenar as tarefas desfeitas para refazer
tarefas_refazer = [] 
