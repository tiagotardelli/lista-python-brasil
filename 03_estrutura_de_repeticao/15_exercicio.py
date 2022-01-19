quanidade = int(input('Digite a quantidade de n: '))

primeiro = segundo = terceiro = 0
for i  in range(quanidade):
    if i == 0:
        primeiro = 1
        print('1')
    elif i == 1:
        segundo = 1
        print('1')  
    else:
        terceiro = primeiro + segundo
        print(f'{terceiro}')
        primeiro = segundo
        segundo = terceiro 
