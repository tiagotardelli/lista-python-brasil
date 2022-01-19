quantidade = int(input('Digite a quantidade de vezes que quer executar o programa: ')) 
for i in range(1, quantidade + 1):
    numero_fatorial = 0
    while True:
        try:
            numero_fatorial = int(input(f'Digite o valor {i}: ')) 
            assert 0 <= numero_fatorial <= 16
            break
        except ValueError:
            print('Deve-se digitar um valor inteiro entre 0 e 16')
        except AssertionError:
            print('Deve-se digitar um valor inteiro entre 0 e 16')
    resultado_int =  numero_fatorial
    resultado_str = str(numero_fatorial) + '!=' + str(numero_fatorial)
    for i in range(1, numero_fatorial):
        numero_fatorial -= 1
        resultado_int *= numero_fatorial
        if numero_fatorial > 0:
            resultado_str = resultado_str + '.' + str(numero_fatorial)       
    print(resultado_str + '=' + str(resultado_int))
