maximo = 0.0

for _ in range(5):
    maximo = max(maximo, float(input('Digite um número: ')))
    
print(f'Número máximo encontrado é: {maximo}')
