"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
cpf_enviado_usuario = '74682489070'
nove_digitos = cpf_enviado_usuario[:9]
dez_digitos = cpf_enviado_usuario [:10]
contador_regressivo_1 = 10
contador_regressivo_2 = 11

resultado_digito_1 = 0
resultado_digito_2 = 0

for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print ( digito_1 )

for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 11) %11
digito_2 = digito_2 if digito_2 <= 9 else 0
print ( digito_2 )

cpf_autenticado = f'{nove_digitos} {digito_1} {digito_2}'

if cpf_enviado_usuario == cpf_autenticado:
    print ( f'{cpf_enviado_usuario} é válido!' )
else:
    print ( f'{cpf_enviado_usuario} este CPF não é válido!' )