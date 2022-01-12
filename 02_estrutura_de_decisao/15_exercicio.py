primeiro_lado_triangulo = float(input('Digite o primeiro lado do triângulo: '))
segundo_lado_triangulo = float(input('Digite o segundo lado do triângulo: '))
terceiro_lado_triangulo = float(input('Digite o terceiro lado do triângulo: '))
if (
    ((primeiro_lado_triangulo + segundo_lado_triangulo) > terceiro_lado_triangulo) and
    ((primeiro_lado_triangulo + terceiro_lado_triangulo) > segundo_lado_triangulo) and
    ((segundo_lado_triangulo + terceiro_lado_triangulo) > primeiro_lado_triangulo)  
    ):
    print('Pode ser um Triângulo')
    if primeiro_lado_triangulo == segundo_lado_triangulo == terceiro_lado_triangulo:
        print("O Triângulo é Equilátero")
    elif (primeiro_lado_triangulo == segundo_lado_triangulo or
        primeiro_lado_triangulo == terceiro_lado_triangulo or
        segundo_lado_triangulo == terceiro_lado_triangulo):
        print("O Triângulo é Isósceles")
    else:
        print("O Triângulo é Escaleno")
else:
    print("Não pode ser um Triângulo")
