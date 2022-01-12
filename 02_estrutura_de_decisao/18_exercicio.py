data = input("Digite uma data no formato 'dd/mm/aaaa': ")
validacao_data = True
if len(data) != 10:
    validacao_data = False
elif 1 < int(data[3:5]) > 12:
    validacao_data = False
elif 1 < int(data[:2]) > 31:
    validacao_data = False
elif (int(data[3:5]) == 4 or int(data[3:5]) == 6 or int(data[3:5]) == 11) and int(data[:2]) > 30:
    validacao_data = False
elif int(data[3:5]) == 2 and int(data[:2]) > 29:
    validacao_data = False
elif (int(data[3:5]) == 2 and int(data[:2]) == 29 and 
    int(data[-4:]) != 0 and 
    (int(data[-4:]) % 400 != 0  if int(data[-4:]) % 100 == 0 else False)
):
    validacao_data = False
if validacao_data:
    print(f'{data} é uma data válida')
else:
    print(f'{data} é uma data inválida')   