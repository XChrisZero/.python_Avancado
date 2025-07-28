"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro."""

"""
R1:
entrada = input ( "Digite um numero inteiro: " ) 

if entrada.isdigit():
    entrada_int = int(entrada)
    entrada_par = entrada_int % 2 ==0 
    par_impar_texto = 'impar'

    if entrada_par:
        par_impar_texto = 'par' 

    print ( f'o numero {entrada} é {par_impar_texto}' )
else:
   print ( f'isso {entrada} não é um numero' )

   
R2:
entrada = input ( "Digite um numero inteiro: " ) 
try:
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')
    """











"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
"""
R:
entrada = input ('Digite a hora')

try:
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    elif hora == 24:
        print('meia noite')
    else:
        print ('não conheço essa hroa')

except:
    print ('digite apenas numeros inteiros!')

"""


















"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
"""
R:

nome = input ('Digite seu nome: ')
tamanho_input = len(nome)

if tamanho_input > 1:
    if tamanho_input <= 4:
        print ("Seu nome é muito curto")
    elif tamanho_input >=5 and tamanho_input <= 6:
        print ("Seu nome é normal")
    else:
        print ("Seu nome é muito grande")
else:
    print("Digite mais de uma letra")

    
"""