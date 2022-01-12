primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
media_nota = (primeira_nota + segunda_nota) / 2
conceito = None
if 9.0 < media_nota <= 10.0:
    conceito = 'A Aprovado'
elif 7.5 < media_nota <= 9.0:
    conceito = 'B Aprovado'
elif 6.0 < media_nota <= 7.5:
    conceito = 'C Aprovado'
elif 4.0 < media_nota <= 6.0:
    conceito = 'D Reprovado'
else:
    conceito = 'E Reprovado'
print(
f"""Nota 1: {primeira_nota:.2f}
Nota 2: {segunda_nota:.2f}
Média: {media_nota:.2f}
Conceito: {conceito}"""
)
