from math import ceil, floor

AREA_FOLGA = 1.1
UM_LITRO_PINTA = 6
LITROS_LATA = 18
VALOR_LATA = 80.0
LITROS_GALAO =  3.6
VALOR_GALAO = 25.0


metros_quadrados = int(input('Digite o tamanho da área a ser pintada em m²: '))
area_com_folga = metros_quadrados * AREA_FOLGA
litros_para_pintar = area_com_folga / UM_LITRO_PINTA

quantidade_lata = ceil(litros_para_pintar / LITROS_LATA)
valor_pagar_lata = quantidade_lata * VALOR_LATA

quantidade_galao = ceil(litros_para_pintar / LITROS_GALAO)
valor_pagar_galao = quantidade_galao * VALOR_GALAO

quantidade_lata_mix = floor(litros_para_pintar / LITROS_LATA)
resto_lata_mix = litros_para_pintar % LITROS_LATA
quantidade_galao_mix = ceil(resto_lata_mix / LITROS_GALAO)
valor_lata_mix = quantidade_galao_mix * VALOR_GALAO
valor_galao_mix = quantidade_lata_mix * VALOR_LATA
soma_mix = valor_lata_mix + valor_galao_mix

print(
    f"""
    Você vai precisar de {quantidade_lata} latas com 18 litros e pagar R$ {valor_pagar_lata}
    Você vai precisar de {quantidade_galao} galões com 3.6 litros e pagar R$ {valor_pagar_galao}
    Você vai precisar no mix de {quantidade_galao_mix} galões com 3.6 litros e {quantidade_lata_mix} latas de 18 litros.
    Você que irá pagar no mix R$ {soma_mix}
    """
)
