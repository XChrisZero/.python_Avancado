# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import aula97_m
#from aula97_m import variavel

print('Este módulo se chama', __name__) # __name__ é uma variável que contém o nome do módulo atual

print('Variável do módulo aula97:', aula97_m.variavel) # Variável do módulo aula97_m importada

resultado = aula97_m.soma(2, 3) # Chamada da função soma do módulo aula97_m
print('Resultado da soma:', resultado)