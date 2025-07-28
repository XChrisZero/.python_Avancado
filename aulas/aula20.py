p_valor1 = input ( "Digite um valor: " )
p_valor2 = input ( "Digite outro valor: " )

pv1 = int(p_valor1)
pv2 = int(p_valor2)

"f-strings"
linha_1 = f'O primeiro valor: {pv1} é maior ou igual que o segundo valor: {pv2}'
linha_2 = f'{pv2} é o maior!'


if pv1 >= pv2:
    print(linha_1)

else:
    print(linha_2)