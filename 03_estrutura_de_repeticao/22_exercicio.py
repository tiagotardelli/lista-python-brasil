numero = 0

while True:
    try:
        numero = int(input('Digite um número inteiro para descobrir se ele é primo: '))   
        assert 1 < numero
        break
    except ValueError:
        print('Deve-se digitar um valor maior que 1')
    except AssertionError:
        print('Deve-se digitar um valor inteiro')

numero_primo = divisivel_por_1 = divisivel_por_si = divisivel_outro = False
divisivel_por = ''

for i in range(1,numero + 1):
    if i == 1 and numero % 1 == 0:
        divisivel_por_1 = True
    elif i == numero and numero % i == 0:
        divisivel_por_si = True
    elif numero % i == 0:
        divisivel_outro = True
        if divisivel_por == '':
            divisivel_por = '. É divisível por: ' + str(i)
        else:
            divisivel_por = divisivel_por + ',' + str(i)
    
numero_primo = ('é primo' if divisivel_por_1 and divisivel_por_si and not divisivel_outro else 'não é primo')
print(f'O {numero} {numero_primo} {divisivel_por}')
