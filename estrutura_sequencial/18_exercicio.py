from math import ceil

QUANTIDADE_MBPS_EM_MB = 0.125

tamanho_arquivo_mb = int(input('Digite o tamanho do arquivo para download em MB: '))
velocidade_link_internet = int(input('Digite a velocidade da internet em Mbps: '))
calcular_velocidade = (tamanho_arquivo_mb / (velocidade_link_internet / 8))
converter_em_minutos = ceil(calcular_velocidade / 60)
print(
    f'O tempo de download de {tamanho_arquivo_mb} MB '
    f'na velocidade de {velocidade_link_internet} '
    f'é próximo de {converter_em_minutos} minuto(s)'
)
