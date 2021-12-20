from math import ceil

UM_LITRO_PINTA = 3
LITROS_LATA = 18
VALOR_LATA = 80.0

metros_quadrados = float(input('Digite o tamanho da área a ser pintada em m²: '))
litros_para_pintar = metros_quadrados / UM_LITRO_PINTA
quantidade_latas = ceil(litros_para_pintar / LITROS_LATA)
valor_pagar = quantidade_latas * VALOR_LATA
print(f'Você vai precisar de {quantidade_latas} latas e pagará R$ {valor_pagar} ')
