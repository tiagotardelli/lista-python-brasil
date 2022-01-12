numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))
numero_3 = float(input('Digite o terceiro número: '))
if numero_2 < numero_1 > numero_3:
    if numero_2 > numero_3:
        print(f'{numero_1} é o maior e {numero_3} é o menor')
    else:
        print(f'{numero_1} é o maior e {numero_2} é o menor')
elif numero_1 < numero_2 > numero_3:
    if numero_1 > numero_3:
        print(f'{numero_2} é o maior e {numero_3} é o menor')
    else:
        print(f'{numero_2} é o maior e {numero_1} é o menor')
elif numero_1 > numero_2:
    print(f'{numero_3} é o maior e {numero_2} é o menor')         
else:
    print(f'{numero_3} é o maior e {numero_1} é o menor')
