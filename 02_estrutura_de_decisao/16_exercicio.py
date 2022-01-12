valor_a = float(input('Digite o valor de a: '))
if valor_a != 0:
    valor_b = float(input('Digite o valor de b: '))
    valor_c = float(input('Digite o valor de c: '))
    calculo_delta = (valor_b ** 2) - (4 * (valor_a * valor_c))
    if calculo_delta < 0:
        print(f"O delta é {calculo_delta:.2f}. A equação não possui raizes reais.")
    elif calculo_delta == 0:
         print(f"O delta é {calculo_delta:.2f}. A equação não possui apenas uma raiz real.")
    else:
        print(f"O delta é {calculo_delta:.2f}. A equação possui duas raizes reais.")
else:
    print("A igual a 0. Não se caracteriza como uma equação de segundo grau.")
