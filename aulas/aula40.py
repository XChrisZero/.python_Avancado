# Calculadora com WHILE
while True:

    primeira_entrada = input ( 'Digite um numero: ' )
    operador = input ( 'Digite qual operador(+)(-)(*)(/) deseja usar: ' )
    segunda_entrada = input ( 'Digite o segundo numero: ' )

    numeros_validos = None

    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float ( primeira_entrada )
        numero_2_float = float ( segunda_entrada )
        numeros_validos = True

    except Exception as error:
        print ( error )

    if numeros_validos is None:
        print ( 'um ou amnos dos numeros não é validos!' )
        continue

    operadores_permitidos = '+-*/' 

    if operador not in operadores_permitidos:
        print ( 'Operador invalido!' )
        continue

    if len(operador) > 1:
        print ( 'Digite apenas 1 operador!' )
        continue
    
    if primeira_entrada and segunda_entrada and operador:
        
        if '+':
            numero_1_float + numero_2_float 
            resultado_mais = numero_1_float + numero_2_float
            print ( f'{primeira_entrada}+{segunda_entrada}={resultado_mais}' )

        elif '-':
            numero_1_float - numero_2_float 
            resultado_menos = numero_1_float - numero_2_float
            print ( f'{primeira_entrada}-{segunda_entrada}={resultado_menos}' )
        
        elif '*':
            numero_1_float * numero_2_float 
            resultado_veses = numero_1_float * numero_2_float
            print ( f'{primeira_entrada}*{segunda_entrada}={resultado_veses}' )
        
        else:
            numero_1_float / numero_2_float 
            resultado_dividido = numero_1_float / numero_2_float
            print ( f'{primeira_entrada}/{segunda_entrada}={resultado_dividido}' )













    sair = input( 'Deseja sair? [S]im ou [N]ão ' ) # poderia chamar o .upper eo .startswith nesta linha 
    sair = sair.upper() # upper converte tudo para maisculo 
    sair = sair.startswith('S') #startsitth para saber se começa com...
    print(sair)

    if sair is True:
        break