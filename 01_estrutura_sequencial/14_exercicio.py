PESO_EXCEDENTE = 50.0
MULTA_EXCEDENTE = 4.0

peso_pesca = float(input('Digite o peso da pesca: '))
excesso = 0.0
multa = 0.0
if peso_pesca > PESO_EXCEDENTE:
    excesso = peso_pesca - PESO_EXCEDENTE
    multa = excesso * MULTA_EXCEDENTE
print(f'Excesso de {excesso} kg e multa de R$ {multa}')
