tipo_combustivel = input('Escolha A-álcool e G-gasolina: ')
quantidade_litros = float(input('Digite a quantidade de litros: '))
valor_litro_alcool = 1.90
valor_litro_gasolina = 2.5
if quantidade_litros <= 20 and tipo_combustivel == 'A':
    valor_com_desconto = (quantidade_litros * valor_litro_alcool) / 1.03
    print(f'O valor a ser pago por {quantidade_litros} litro(s) de Álcool será de R$ {valor_com_desconto:.2f}')
elif quantidade_litros > 20 and tipo_combustivel == 'A':
    valor_com_desconto = (quantidade_litros * valor_litro_alcool) / 1.05
    print(f'O valor a ser pago por {quantidade_litros} litro(s) de Álcool será de R$ {valor_com_desconto:.2f}')
elif quantidade_litros <= 20 and tipo_combustivel == 'G':
    valor_com_desconto = (quantidade_litros * valor_litro_gasolina) / 1.04
    print(f'O valor a ser pago por {quantidade_litros} litro(s) de Gasolina será de R$ {valor_com_desconto:.2f}')
elif quantidade_litros > 20 and tipo_combustivel == 'G':
    valor_com_desconto = (quantidade_litros * valor_litro_gasolina) / 1.06
    print(f'O valor a ser pago por {quantidade_litros} litro(s) de Gasolina será de R$ {valor_com_desconto:.2f}')
