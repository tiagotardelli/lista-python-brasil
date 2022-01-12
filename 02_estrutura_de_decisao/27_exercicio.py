quantidade_morango = float(input('Quantidade de morangos em Kg: ')) 
quantidade_maca = float(input('Quantidade de maça em Kg: ')) 
valor_pagar_morango = valor_pagar_maca = valor_a_pagar = quantidade_frutas = 0.0

if quantidade_morango <= 5:
    valor_pagar_morango = quantidade_morango * 2.5
elif quantidade_morango > 5:
    valor_pagar_morango = quantidade_morango * 2.2

if quantidade_maca <= 5:
    valor_pagar_maca = quantidade_maca * 1.8
elif quantidade_morango > 5:
    valor_pagar_maca = quantidade_maca * 1.5

valor_a_pagar = valor_pagar_maca + valor_pagar_morango
quantidade_frutas = quantidade_maca + quantidade_morango

if valor_a_pagar > 25 or quantidade_frutas > 8:
        valor_a_pagar = valor_a_pagar / 1.1
print(f'Valor a ser pago é: R$ {(valor_a_pagar):.2f}')
