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

# Listas para armazenar as tarefas e as tarefas desfeitas
tarefas = []

# Lista para armazenar as tarefas desfeitas para refazer
tarefaz_refazer = [] 

