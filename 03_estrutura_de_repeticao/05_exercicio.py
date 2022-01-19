import math


populacao_pais_a = populacao_pais_b = taxa_crescimento_a = taxa_crescimento_b = anos = 0
validado = 0
continuar = True

while True:
    try:
        if validado == 0:
            populacao_pais_a = int(input('Digite o valor da populacão A: '))
            assert populacao_pais_a > 0 
            validado +=1
        if validado == 1:
            populacao_pais_b = int(input('Digite o valor da populacão B: '))
            assert populacao_pais_b > 0 
            validado +=1
        if validado == 2:
            taxa_crescimento_a = float(input('Digite a taxa de crescimento da populacão A: '))
            assert taxa_crescimento_a > 0 
            validado +=1
        if validado == 3:
            taxa_crescimento_b = float(input('Digite a taxa de crescimento da populacão B: '))
            assert taxa_crescimento_b > 0
            validado +=1 
        if validado == 4:
            while populacao_pais_a < populacao_pais_b:
                anos += 1
                populacao_pais_a = math.floor(populacao_pais_a + (populacao_pais_a * (taxa_crescimento_a / 100)))
                populacao_pais_b = math.floor(populacao_pais_b + (populacao_pais_b * (taxa_crescimento_b / 100)))

            print(
                f"""Levarão {anos} anos
                Para A chegar a {populacao_pais_a}
                Para B chegar a {populacao_pais_b}"""
            )
            while True:
                try:
                    executar_novamente =  input('Deseja executar novamente (S/N)?: ')
                    assert executar_novamente in ('S', 'N') 
                except AssertionError:
                    print("Deve ser informado 'S' ou 'N'")
                else:
                    continuar = (True if executar_novamente == 'S' else False)
                    validado = 0
                    break
        if not continuar:
            print('Fim do Programa.')
            break
            
    except ValueError:
        print('Deve ser fornecido um valor inteiro')
    except AssertionError:
        print('Deve ser fornecido um valor maior que 0')
