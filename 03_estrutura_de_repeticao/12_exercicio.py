numero = int(input('Digite um valor ente 1 e 10: '))
print(f'Tabuada do {numero}')

for i in range(1,11):
    print(f'{numero} X {i} = {int(numero*i)}')
    