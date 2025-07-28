"""
Iterável -> str, range, etc __iter__() é um elemento que tem um metodo iter dentro dele 
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
.__iter__() == iter()
"""
# for(para cada) letra in(no) texto... letra é uma variaaavel criada no for para absorver cada letra dessa string
texto = 'Luiz'  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)