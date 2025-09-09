# Problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None): # Nunca usar lista=[] como valor padrão
    if lista is None: # Assim evitamos o problema
        lista = [] # Criamos uma nova lista a cada chamada sem lista
    lista.append(nome) 
    return lista


cliente1 = adiciona_clientes('luiz') # Primeira chamada, cria nova lista
adiciona_clientes('Joana', cliente1) # Reutiliza a lista cliente1
adiciona_clientes('Fernando', cliente1) # Reutiliza a lista cliente1
cliente1.append('Edu') # Modifica a lista cliente1

cliente2 = adiciona_clientes('Helena') # Segunda chamada, cria nova lista
adiciona_clientes('Maria', cliente2) # Reutiliza a lista cliente2

cliente3 = adiciona_clientes('Moreira') # Terceira chamada, cria nova lista
adiciona_clientes('Vivi', cliente3) # Reutiliza a lista cliente3

print(cliente1)
print(cliente2)
print(cliente3)