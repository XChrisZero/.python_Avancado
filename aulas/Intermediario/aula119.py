# Exercício - Lista de tarefas com desfazer e refazer
from exercicios.exercicio_119 import listar, desfazer, refazer, adicionar, ler, salvar, sair, tarefas, tarefas_refazer
import os
import json

# Caminho do arquivo JSON para salvar as tarefas
CAMINHO_ARQUIVO = 'aula119.json'
tarefas = ler([], CAMINHO_ARQUIVO) # Lê as tarefas do arquivo JSON
tarefas_refazer = [] # Lista para armazenar as tarefas desfeitas

print ( 'Lista de tarefas!' )
while True: # Loop infinito para o usuário adicionar tarefas

    print ( 'Comandos: \r\n[L]istar, [D]esfazer ou [R]efazer [S]air ', end= '\n \r-------------------------------\n \r' )

    tarefa = input ( 'Digite um dos comandos acima ou uma tarefa: ' ) 

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
        'sair': sair,
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)


#    if tarefa == 'L': # Listar as tarefas
#        listar(tarefas) 
#        continue # Volta para o início do loop
#    elif tarefa == 'D': # Desfazer a última tarefa
#        desfazer(tarefas, tarefaz_refazer)
#        listar(tarefas)
#        continue
#    elif tarefa == 'R': # Refazer a última tarefa desfeita
#        refazer(tarefas, tarefaz_refazer)
#        listar(tarefas)
#        continue
#    elif tarefa == 'cls': # Limpar a tela
#        os.system( 'cls' )
#        continue
#    elif tarefa == 'S': # Sair do programa
#        break
#    else: # Adicionar uma nova tarefa
#        adicionar(tarefa, tarefas)
#        listar(tarefas)
#        continue
