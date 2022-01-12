print(
    """
        M - Matutino
        V - Vespertino
        N - Noturno
    """
)
turno_estuda = input('Digite o turno que você estuda: ')
if turno_estuda == 'M':
    print('Bom dia!')
elif turno_estuda == 'V':
    print('Boa Tarde!')
elif turno_estuda == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')
