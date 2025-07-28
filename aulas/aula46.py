for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('chegou no 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
        
    for k in range(1, 3, 5):
        print(i, j, k)
else:
    print('For completo com sucesso!')