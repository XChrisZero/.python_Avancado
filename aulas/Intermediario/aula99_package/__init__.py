'''print (
f" Você importou o {__name__} "
)

'''

from aula99_package.modulo import * # Importando tudo do módulo e nesse caso não se encaixa como má prática, pois é um exemplo de uso de pacotes.
# fazendo isso, todas as funções e variáveis do módulo estarão disponíveis diretamente no namespace do pacote.
# https://stackoverflow.com/questions/2386714/why-is-import-bad

from aula99_package.modulo_b import *  # Importando tudo do módulo_b, assim como no módulo anterior.
# Isso permite que você use as funções e variáveis definidas nesses módulos diretamente, sem precisar referenciar o nome do módulo.