from math import ceil

UM_LITRO_PINTA = 6
LITROS_LATA = 18
VALOR_LATA = 80.0
LITROS_GALAO =  3.6
VALOR_GALAO = 25.0
QUANTIDADE_GALAO_INDICADO = 3
LITROS_GALAO_INDICADO = 10.8

metros_quadrados = float(input('Digite o tamanho da área a ser pintada em m²: '))
litros_para_pintar = metros_quadrados / UM_LITRO_PINTA
quantidade_lata = ceil(litros_para_pintar / LITROS_LATA)
valor_pagar_lata = quantidade_lata * VALOR_LATA
quantidade_galao = ceil(litros_para_pintar / LITROS_LATA)
valor_pagar_galao = quantidade_galao * VALOR_GALAO
litros_para_pintar_mix = ceil(litros_para_pintar + (litros_para_pintar * 0.1))
quantidade_galao_mix = 0
quantidade_lata_mix = 0

if litros_para_pintar_mix <= LITROS_GALAO_INDICADO:
        quantidade_galao_mix = ceil(litros_para_pintar_mix / LITROS_GALAO)
else:
    lata_resto = ceil(litros_para_pintar_mix % LITROS_LATA)
    if lata_resto >= LITROS_GALAO_INDICADO:
        quantidade_lata_mix = ceil(litros_para_pintar_mix - lata_resto) / LITROS_LATA
    else:
        quantidade_lata_mix = ceil((litros_para_pintar_mix - lata_resto) / LITROS_LATA)
        quantidade_galao_mix = ceil(lata_resto / LITROS_GALAO)

valor_lata_mix = float(quantidade_galao_mix) * VALOR_GALAO
valor_galao_mix = float(quantidade_lata_mix) * VALOR_LATA
soma_mix = valor_lata_mix + valor_galao_mix
print(
    f"""
    Você vai precisar de {quantidade_galao} galões com 3.6 litros e pagar R$ {float(valor_pagar_galao)}
    Você vai precisar de {quantidade_lata} latas com 18 litros e pagar R$ {float(valor_pagar_lata)}
    Você vai precisar no mix de {quantidade_galao_mix} galões com 3.6 litros e {quantidade_lata_mix} latas de 18 litros.
    Você vai paga no mix R$ {float(soma_mix)}
    """
)
