# Exercício - Adiando execução de funções
from exercicios import criar_funcao, soma, multiplica

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))
