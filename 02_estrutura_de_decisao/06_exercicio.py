numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))
numero_3 = float(input('Digite o terceiro número: '))
if numero_2 < numero_1 > numero_3:
    print(f'O {numero_1} é o maior número.')
elif numero_1 < numero_2 > numero_3: 
    print(f'O {numero_2} é o maior número.')
else:
    print(f'O {numero_3} é o maior número.')
