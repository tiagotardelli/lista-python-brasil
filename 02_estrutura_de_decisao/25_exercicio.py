pergunta_1 = (1 if input("Telefonou para a vítima? S/N: ") == 'S' else 0)
pergunta_2 = (1 if input("Esteve no local do crime? S/N: ") == 'S' else 0)
pergunta_3 = (1 if input("Mora perto da vítima? S/N: ") == 'S' else 0)
pergunta_4 = (1 if input("Devia para a vítima? S/N: ") == 'S' else 0)
pergunta_5 = (1 if input("Já trabalhou com a vítima? S/N: ") == 'S' else 0)

soma_perguntas =  pergunta_1 + pergunta_2 + pergunta_3 + pergunta_4 + pergunta_5
if soma_perguntas == 5:
    print('Assassino')
elif 3<= soma_perguntas <=4:
    print('Cúmplice')
elif soma_perguntas == 2:
    print('Suspeita')
else:
    print('Inocente')
