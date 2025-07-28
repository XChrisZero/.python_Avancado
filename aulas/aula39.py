"""
Iterando strings com while
"""
#       012345678910
nome = 'Christian Kuriak Chung Ferrari'  # Iteráveis

indice = 0
nova_string = ''

while indice < len(nome):
 
 letra = nome[indice]
 nova_string += f'* {letra} '
 
  
 indice += 1
    
 print ( nova_string ) #só por estar printando dentro do loop cria o efeito!



print ( nova_string )

 
