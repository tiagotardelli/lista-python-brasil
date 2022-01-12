nota_parcial_1 = float(input('Digite a primeira nota parcial: '))
nota_parcial_2 = float(input('Digite a segunda nota parcial: '))
nota_parcial_3 = float(input('Digite a terceira nota parcial: '))
media_notas = (nota_parcial_1 + nota_parcial_2 + nota_parcial_3) / 3
if media_notas >= 7:
    if media_notas == 10:
        print(f'Aprovado com Distinção com a média de {media_notas:.2f}')
    else:
        print(f'Aprovado com a média de {media_notas:.2f}')
elif media_notas < 7:
     print(f'Reprovado com a média de {media_notas:.2f}')
