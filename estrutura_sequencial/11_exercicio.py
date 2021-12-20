numero_1_inteiro = int(input('Digite um número inteiro: '))
numero_2_inteiro = int(input('Digite outro número inteiro: '))
numero_3_real = float(input('Digite um número real: '))
dobro_num1_metade_num2 = (numero_1_inteiro * 2) + (numero_2_inteiro / 2)
triplo_num1_soma_num3 = (numero_1_inteiro * 3) + numero_3_real
num3_elevado_cubo = numero_3_real ** 3
print(
    f"""
    Valor numero 1: {numero_1_inteiro}
    Valor numero 2: {numero_2_inteiro}
    Valor numero 3: {numero_3_real}
    O produto do dobro do primeiro com metade do segundo: {dobro_num1_metade_num2}
    A soma do triplo do primeiro com o terceiro: {triplo_num1_soma_num3}
    O terceiro elevado ao cubo: {num3_elevado_cubo}
    """
)
