import importlib # importlib é usado para importar módulos dinamicamente, sem ela o mudulo aula98_m não seria recarregado

import aula98_m

print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m) # reload é usado para recarregar o módulo
    print(i)

print('Fim')