numero_base = int(input('Digite o número de base: '))
numero_expoente = int(input('Digite o número do expoente: '))
resultado_potencia = 1

for _ in range(numero_expoente):
    resultado_potencia *= numero_base 

print(f'{numero_base} elevado a {numero_expoente} é: {resultado_potencia}')
