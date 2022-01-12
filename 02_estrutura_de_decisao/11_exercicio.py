salario_atual = float(input('Digite o salário do colaborador: '))
percentual_aumento = 0
if salario_atual <= 280.00:
    percentual_aumento = (20 / 100)
elif 280.0 < salario_atual <= 700.0:
    percentual_aumento = (15 / 100)
elif 700.0 < salario_atual <= 1500.0:
    percentual_aumento = (10 / 100)
else:
    percentual_aumento = (5 / 100)
valor_aumento = salario_atual * percentual_aumento
salario_reajustado = salario_atual + valor_aumento 
print(f"""Salário Atual: R$ {salario_atual}
Percentual de Aumento Aplicado: {int(percentual_aumento*100)}%
Valor de Aumento: {valor_aumento}
Salário com Aumento: R$ {salario_reajustado}""")
