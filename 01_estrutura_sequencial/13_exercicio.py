altura = float(input('Digita a sua altura: '))
calculo_peso_ideal_homem =  (72.7 * altura) - 58
calculo_peso_ideal_mulher =  (62.1 * altura) - 44.7
print(
    f"""
    ## Cálculo de Peso Ideal ##
    Para a atura de {altura} :
        * Para homens: {calculo_peso_ideal_homem}
        * Para mulheres: {calculo_peso_ideal_mulher}
    """
    )
