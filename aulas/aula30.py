"""Add commentMore actions
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 90  # velocidade atual do carro
local_carro = 75  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

if velocidade >= 61 and local_carro == 100:
    print ( "Você está acima da velocidade masxima da via.")

else:
    print ( " ainda está em uma velocidade adequada." )