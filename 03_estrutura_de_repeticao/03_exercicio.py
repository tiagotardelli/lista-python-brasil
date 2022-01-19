nome_valido = idade_valida = salario_valido = sexo_valido =  estado_civil_valido = False

while True:
    if not nome_valido:
        nome = input('Digite um nome com 3 ou mais letras: ')
        if len(nome) >= 3:
            nome_valido = True
        else:
            print('Nome deve ter 3 ou mais letras!')

    if not idade_valida and nome_valido:
        idade = int(input('Digite uma idade entre 0 e 150: '))
        if 0 < idade < 150:
            idade_valida = True
        else:
            print('Idade deve estar entre 0 a 150')
    if not salario_valido and idade_valida:
        salario = float(input('Digite um salário maior que 0: '))
        if salario > 0:
            salario_valido = True
        else:
            print('Salário deve ser maior que 0')

    if not sexo_valido and salario_valido:
        sexo = input("Digite 'm' para masculino ou 'f' para feminino: ")
        if sexo == 'f' or sexo == 'm':
            sexo_valido = True
        else:
            print('Sexo deve ser f ou m')

    if not estado_civil_valido and sexo_valido:
        estado_civil = input("Digite 's' (solteiro(a)), 'c' (casado(a)), 'v' (viúvo(a)) ou 'd' (divorciado(a)) :")
        if (estado_civil == 's' or 
        estado_civil == 'c' or
        estado_civil == 'v' or
        estado_civil == 'd'):
            estado_civil_valido = True
        else:
            print('Estado Civil deve ser s, c, v ou d')

    if (nome_valido and idade_valida and salario_valido and sexo_valido and estado_civil_valido):
        print(f'Nome: {nome}\n'
        f'Idade: {idade}\n'
        f'Salário: R$ {salario:.2f}\n'
        f'Sexo: {sexo}\n'
        f'Estado Civil: {estado_civil}')
        break
