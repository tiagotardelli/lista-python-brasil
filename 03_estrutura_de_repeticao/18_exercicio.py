quantidade = int(input('Digite a quantidade de números do conjunto: ')) 
menor_valor = maior_valor = soma = 0

for i in range(1, quantidade + 1):
    valor_atual = float(input(f'Digite o valor {i}: '))

    if i == 1: 
        menor_valor = valor_atual
        maior_valor = valor_atual

    if menor_valor > valor_atual:
        menor_valor = valor_atual

    if maior_valor < valor_atual:
        maior_valor = valor_atual
    
    soma += valor_atual 

print(
    f"""Menor valor: {menor_valor}
Maior valor: {maior_valor}
Soma: {soma}"""
)
