valor_hora = float(input('Digite o valor que você ganha por hora: '))
quantidade_horas = float(input('Digite a quantidade de horas trabalhadas: '))
salario_bruto = quantidade_horas * valor_hora
imposto_de_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (imposto_de_renda + inss + sindicato)
print(
    f"""
    + Salário Bruto : R$ {salario_bruto}
    - IR (11%) : R$ {imposto_de_renda}
    - INSS (8%) {inss}
    - Sindicato (5%) : {sindicato}
    = Salário Líquido : R$ {salario_liquido}    
    """
)
