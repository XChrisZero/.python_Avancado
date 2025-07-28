senha_salva = '123456'
senha_digitada = ''
repeticoes = 1

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')

    repeticoes += 1
    if repeticoes == 4:
        print (f'você bateu o limite de tentativas')
        break

