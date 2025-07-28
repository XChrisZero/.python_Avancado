'''
texto = 'Eu amo o Python'
for letra in texto:
    print (texto) 
o for trabalha assim por baixo dos panos:
'''
texto = 'Eu amo o Python' #iteravel
iterador = texto.__iter__ #iterator
iterador = iter(texto) #iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break


"""
Iterator -> quem sabe entregar um valor por vez
next() -> me entregue o próximo valor
iter() ou .__iter__ -> me entregue seu iterador

"""