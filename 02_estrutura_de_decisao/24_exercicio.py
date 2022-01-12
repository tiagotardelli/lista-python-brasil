numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))
operacao = 'divisao'

if operacao == 'adicao':
    resultado = (numero_1 + numero_2)
elif operacao == 'subtracao':
    resultado = (numero_1 - numero_2)
elif operacao == 'multiplicacao':
    resultado = (numero_1 * numero_2)
elif operacao == 'divisao':
    resultado = (numero_1 / numero_2)

print(f"O resultado {resultado} {'é par' if resultado % 2 == 0 else 'é ímpar' }\n"
f"O resultado {resultado} {'é positivo' if resultado >= 0 else 'é negativo'}\n"
f"O resultado {resultado} {'é inteiro' if round(resultado) == resultado else 'é decimal'}")
