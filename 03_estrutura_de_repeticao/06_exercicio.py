exibicao = int(input('Digite 0 - Exibir um abaixo do outro ou 1 - Exibir um do lado do outro: '))

if exibicao == 0:
    for i in range(1,21):
        print(f'{i}')
elif exibicao == 1:
    exibir = ''
    for i in range(1,21):
        exibir = exibir + ' ' + str(i)
    print((exibir.lstrip()).rstrip())
