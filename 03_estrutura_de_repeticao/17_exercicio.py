numero = int(input('Digite um número inteiro: '))
resultado_int =  numero
resultado_str = str(numero) + '!=' + str(numero)
for i in range(1, numero):
    numero -= 1
    resultado_int *= numero
    resultado_str = resultado_str + '.' + str(numero)       
print(resultado_str + '=' + str(resultado_int))
