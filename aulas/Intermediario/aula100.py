# copy, sorted, produtos.sort
# Exercícios
# 1.Aumente os preços dos produtos a seguir em 10% 
# 2.Gere novos_produtos por deep copy (cópia profunda) 
# 3.Ordene os produtos por nome decrescente (do maior para menor) 
# 4.Gere produtos_ordenados_por_nome por deep copy (cópia profunda) 
# 5.Ordene os produtos por preco crescente (do menor para maior) 
# 6.Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
from exercicios import produtos
import copy

novos_produtos = [
    { **p, 'preco': p['preco'] * 1.10 } #round para arredondar o valor
    for p in copy.deepcopy(produtos) #produtos[:] também funciona

]

produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)
produtos_ordenados_por_nome.sort(
    key=lambda x: x['nome'],
    reverse=True
)

produtos_ordenados_por_preco = copy.deepcopy(novos_produtos)
produtos_ordenados_por_preco.sort(
    key=lambda x: x['preco'],
)

print('Produtos originais:')
print(*produtos, sep='\n') #* para desempacotar a lista
print()
print('Novos produtos com 10% de aumento:')
print(*novos_produtos, sep='\n')
print()
print('Produtos ordenados por nome (decrescente):') 
print(*produtos_ordenados_por_nome, sep='\n')
print()
print('Produtos ordenados por preço (crescente):')
print(*produtos_ordenados_por_preco, sep='\n')
