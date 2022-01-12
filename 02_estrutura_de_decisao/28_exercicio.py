#print('tipo de carne 1 - File Duplo | 2 - Alcatra | 3 - Picanha \n')
tipo_de_carne = int(input('Digite o tipo da carne: '))
print(tipo_de_carne)
quantidade_de_carne = float(input('Digite a quantidade de carne: '))
#print('tipo de carne 1 - Cartão de Débito | 2 - Cartão de Crédito | 3 - Cartão Tabajara \n')
tipo_de_pagamento = input('Digite o tipo de pagamento: ')
descricao_pagamento = descricao_carne = ''
valor_a_pagar_sem_desconto = valor_unidade_carne = valor_total = desconto = 0.0

print('aqui')
print(tipo_de_carne)
if tipo_de_carne == 1:
    print('passou')
    descricao_carne = 'File Duplo'
    if quantidade_de_carne > 5:
        valor_unidade_carne = 5.8
    else:
        valor_unidade_carne = 4.9
elif tipo_de_carne == 2: 
    descricao_carne = 'Alcatra'
    if quantidade_de_carne > 5:
        valor_unidade_carne = 6.8
    else:
        valor_unidade_carne = 5.9
elif tipo_de_carne == 3:
    descricao_carne = 'Picanha'
    if quantidade_de_carne > 5:
        valor_unidade_carne = 7.8
    else:
        valor_unidade_carne = 6.9

if tipo_de_pagamento == 3:
    descricao_pagamento = 'Cartão Tabajara'
    desconto = 5.0
elif tipo_de_pagamento == 2:
    descricao_pagamento = 'Cartão de Crédito'
    desconto = 0.0
elif tipo_de_pagamento == 1:      
    descricao_pagamento = 'Cartão de Débito'
    desconto = 0.0

valor_a_pagar_sem_desconto = valor_unidade_carne * quantidade_de_carne
valor_do_desconto = valor_a_pagar_sem_desconto * (desconto / 100)
valor_total = valor_a_pagar_sem_desconto - valor_do_desconto

print(
    f"Modo de Pagamento: {descricao_pagamento}\n"
    f"Tipo da Carne: {descricao_carne}\n"
    f"Valor Unidade: R$ {valor_unidade_carne:.2f}\n"
    f"Quantidade: {quantidade_de_carne}\n"
    f"Valor do Desconto: R$ {valor_do_desconto:.2f}\n"
    f"Valor a ser Pago: R$ {valor_total:.2f}"
)
