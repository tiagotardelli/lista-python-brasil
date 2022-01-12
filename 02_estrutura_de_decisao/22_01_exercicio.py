numero_inteiro = int(input('Digite um número inteiro: '))
resto_divisao = numero_inteiro % 2
if resto_divisao == 0:
    print(f'O número {numero_inteiro} é par.')
else:
    print(f'O número {numero_inteiro} é ímpar.')
