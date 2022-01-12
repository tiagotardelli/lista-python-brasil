valor_hora_trabalhada = float(input('Digite o valor hora: '))
quantidade_horas_trabalhada = float(input('Digite a quantidade de horas: '))
salario_bruto = valor_hora_trabalhada * quantidade_horas_trabalhada
taxa_ir = 0
if 900 < salario_bruto <= 1500:
    taxa_ir = 5 / 100
elif 1500 < salario_bruto <= 2500:
    taxa_ir = 10 / 100
elif salario_bruto > 2500:
    taxa_ir = 20 / 100

desconto_ir = salario_bruto * taxa_ir 
desconto_inss = salario_bruto * (10 / 100)
desconto_sindicato = salario_bruto * (3 / 100)
total_desconto = desconto_ir + desconto_inss + desconto_sindicato
fgts_empresa = salario_bruto * (11 / 100)
salario_liquido = salario_bruto - total_desconto
print(
 f"""Salário Bruto ({valor_hora_trabalhada:.2f} * {quantidade_horas_trabalhada:.2f})  : R$ {salario_bruto:.2f}
(-) IR ({int(taxa_ir * 100)}%)                    : R$ {desconto_ir:.2f}
(-) INSS (10%)                  : R$ {desconto_inss:.2f}
(-) Sindicato (3%)              : R$ {desconto_sindicato:.2f}
FGTS (11%)                      : R$ {fgts_empresa:.2f}
Total de descontos              : R$ {total_desconto:.2f}
Salário Líquido                 : R$ {salario_liquido:.2f}"""
) 
