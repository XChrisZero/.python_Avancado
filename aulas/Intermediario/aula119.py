# Exercício - Lista de tarefas com desfazer e refazer
from exercicios.exercicio_119 import listar, desfazer, refazer, adicionar, tarefas, tarefaz_refazer # Importando as funções do outro arquivo
import os

print ( 'Lista de tarefas!' )

while True: # Loop infinito para o usuário adicionar tarefas

    print ( 'Comandos: \r\n[L]istar, [D]esfazer ou [R]efazer [S]air ', end= '\n \r-------------------------------\n \r' )

    tarefa = input ( 'Digite a inicial de um dos comandos acima ou uma tarefa: ' ) 
    tarefa = tarefa.upper()

    if tarefa == 'L': # Listar as tarefas
        listar(tarefas) 
        continue # Volta para o início do loop

    elif tarefa == 'D': # Desfazer a última tarefa
        desfazer(tarefas, tarefaz_refazer)
        listar(tarefas)
        continue

    elif tarefa == 'R': # Refazer a última tarefa desfeita
        refazer(tarefas, tarefaz_refazer)
        listar(tarefas)
        continue

    elif tarefa == 'cls': # Limpar a tela
        os.system( 'cls' )
        continue

    elif tarefa == 'S': # Sair do programa
        break

    else: # Adicionar uma nova tarefa
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue
    
    

    
    
 

   