"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os
print ('Jogo da forca a dica é ...')
palavra_secreta = 'python'
letra_acertada = ''
contagem_tentativas = 1

while True:
    
    letra_digitada = input( f'{contagem_tentativas}x Digite uma letra:' )
    contagem_tentativas += 1
    
    if len(letra_digitada) > 1:
        print ( 'Digite apenas 1 petra por vez!' )
        continue

    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada

    palavra_formatada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formatada += letra_secreta  
        else:
            palavra_formatada += '*'

    print ( 'Palavra formada: ', palavra_formatada )

    if palavra_formatada == palavra_secreta:
        os.system( 'cls' )
        print ( 'Você acertou a palavra chave!' )
        print ( 'a palavra era', palavra_secreta )
        print ( f'Foram {contagem_tentativas} tentativas para acertar!')
        letra_acertada = ''
        contagem_tentativas = 1
    
