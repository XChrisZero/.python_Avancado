# Exercício - Adiando execução de funções
from exercicios import criar_funcao, soma, multiplica # Importando do __init__.py


soma_com_cinco = criar_funcao(soma, 5) # Adiando a execução da função soma
multiplica_por_dez = criar_funcao(multiplica, 10)# Adiando a execução da função multiplica

print(soma_com_cinco(10))
print(multiplica_por_dez(10))
