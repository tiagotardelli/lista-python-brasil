primeiro = segundo = terceiro = 0
while True:
    if primeiro == 0:
        print('0')
        primeiro = 1
    elif segundo == 0:
        segundo = 1
        print('1')
        print('1')  
    else:
        terceiro = primeiro + segundo
        print(f'{terceiro}')
        primeiro = segundo
        segundo = terceiro 
    if terceiro > 500:
        break
