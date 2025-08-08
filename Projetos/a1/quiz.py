while True:

    perguntas = [
        {
            'Pergunta': 'Quanto é 2+2?',
            'Opções': ['1', '3', '4', '5'],
            'Resposta': '4',
        },
        {
            'Pergunta': 'Quanto é 5*5?',
            'Opções': ['25', '55', '10', '51'],
            'Resposta': '25',
        },
        {
            'Pergunta': 'Quanto é 10/2?',
            'Opções': ['4', '5', '2', '1'],
            'Resposta': '5',
        },
    ]

    quantidade_certas = 0
    for pergunta in perguntas:
        print('Pergunta: ')
        print( pergunta['Pergunta'] )
    
        opcoes = pergunta['Opções']

        for i, opcao in  enumerate(opcoes):
            print(f' {i})', opcao)
        print()

        entrada = input ( 'Escolha uma Opção: ' )
        entrada_int = None

        Certo = False
        quantidade_opcoes = len(opcoes)

        if entrada.isdigit():
            entrada_int = int(entrada)

        if entrada_int is not None:
            if entrada_int >= 0 and entrada_int < quantidade_opcoes:
                if opcoes[entrada_int] == pergunta['Resposta']:
                    Certo = True
        if Certo:
            quantidade_certas += 1
            print ('Boa! Resposta certa')
        else:
            print( 'Pergunta errada!')

    print ()
    print (f'Você acertou {quantidade_certas} de {len(perguntas)} perguntas.')

    sair = input( 'Deseja sair? [S]im ou [N]ão ' ) # poderia chamar o .upper eo .startswith nesta linha 
    sair = sair.upper() # upper converte tudo para maisculo 
    sair = sair.startswith('S') #startsitth para saber se começa com...
    print(sair)

    if sair is True:
        break