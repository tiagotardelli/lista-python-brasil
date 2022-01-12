numero_inteiro = int(input('Digite um número inteiro: '))
if (numero_inteiro & 1) == 0:
    print(f'O número {numero_inteiro} é par.')
elif (numero_inteiro & 1) == 1:
    print(f'O número {numero_inteiro} é ímpar.')
