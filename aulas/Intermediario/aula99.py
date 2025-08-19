#from sys import path  

import aula99_package.modulo #2
from aula99_package import modulo # 3
#from aula99_package.modulo import * #má pratica, mas funciona
from aula99_package.modulo import soma_do_modulo, variavel, nova_variavel # 1


# print(*path, sep='\n')
print(soma_do_modulo(1, 2)) # 1
print(aula99_package.modulo.soma_do_modulo(1, 2)) # 2
print(modulo.soma_do_modulo(1, 2)) # 3
print(variavel)
print(nova_variavel)

print(__name__)
