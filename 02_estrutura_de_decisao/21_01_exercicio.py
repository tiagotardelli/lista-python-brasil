valor_saque = int(input('Digite um valor entre 10 e 600 para saque: '))
valor_saque_str = 'Para sacar a quantia de ' + str(valor_saque) + ' reais, o programa fornece '
valor_valido = True if  10 <= valor_saque <= 600 else False
notas_100_str = notas_50_str = notas_10_str = ''
notas_5_str = notas_1_str = ''
notas_100_int = notas_50_int = notas_10_int = 0
notas_5_int = notas_1_int = ''
notas_5_int = 0
quantia_notas_diferentes = 0 
if valor_valido:
    if valor_saque >= 100:
        notas_100_int, valor_saque = divmod(valor_saque, 100)
        quantia_notas_diferentes += 1
        if notas_100_int == 1:
            notas_100_str = 'uma nota de 100'
        elif notas_100_int == 2:
            notas_100_str = 'duas notas de 100'
        elif notas_100_int == 3:
            notas_100_str = 'três notas de 100'
        elif notas_100_int == 4:
            notas_100_str = 'quatro notas de 100'
        elif notas_100_int == 5:
            notas_100_str = 'cinco notas de 100'
        elif notas_100_int == 6:
            notas_100_str = 'seis notas de 100'
    if valor_saque >= 50:
        notas_50_int, valor_saque = divmod(valor_saque, 50)
        quantia_notas_diferentes += 1
        notas_50_str = 'uma nota de 50'
        
    if valor_saque >= 10: 
        notas_10_int, valor_saque = divmod(valor_saque, 10)
        quantia_notas_diferentes += 1
        if notas_10_int == 1:
            notas_10_str = 'uma nota de 10'
        elif notas_10_int == 2:
            notas_10_str = 'duas notas de 10'
        elif notas_10_int == 3:
            notas_10_str = 'três notas de 10'
        elif notas_10_int == 4:
            notas_10_str = 'quatro notas de 10'
            
    if valor_saque >= 5:
        notas_5_int, valor_saque = divmod(valor_saque, 5)
        quantia_notas_diferentes += 1
        notas_5_str = 'uma nota de 5'
            
    if valor_saque >= 4:
        quantia_notas_diferentes += 1
                
        if valor_saque == 1:
            notas_1_str = 'uma nota de 1'
        if valor_saque == 2:
            notas_1_str = 'duas nota de 1'
        if valor_saque == 3:
            notas_1_str = 'três notas de 1'
        if valor_saque == 4:
            notas_1_str = 'quatro notas de 1'
if not valor_valido:
    print('Saque disponível apenas para valores entre 10 a 600')
elif quantia_notas_diferentes == 1:
    print(valor_saque_str + notas_100_str + notas_50_str + notas_10_str)
elif quantia_notas_diferentes == 2:
    if notas_100_str != '':
            print(f'{valor_saque_str}{notas_100_str} e ' + 
                notas_50_str + notas_10_str + notas_5_str + notas_1_str)
    elif notas_50_str != '':
            print(f'{valor_saque_str}{notas_50_str} e ' + 
                notas_10_str + notas_5_str + notas_1_str)             
    elif notas_10_str != '':
            print(f'{valor_saque_str}{notas_10_str} e ' + 
                notas_5_str + notas_1_str)
elif quantia_notas_diferentes == 3:
    if notas_100_str != '':
        if notas_50_str != '':
            print(f'{valor_saque_str}{notas_100_str}, ' + 
                notas_50_str + ' e ' + notas_10_str + notas_5_str + notas_1_str)
        elif notas_10_str != '':
            print(f'{valor_saque_str}{notas_100_str}, ' + 
                notas_10_str + ' e ' + notas_5_str + ' + ' + notas_1_str)           
        elif notas_5_str != '':
            print(f'{valor_saque_str}{notas_100_str}, ' + 
                notas_5_str + 'e ' + notas_1_str)   
    elif notas_50_str != '':
        if notas_10_str != '':
            print(f'{valor_saque_str}{notas_50_str}, ' + 
                notas_10_str + ' e ' + notas_5_str + notas_1_str)      
        elif notas_5_str != '':
            print(f'{valor_saque_str}{notas_50_str}, ' + 
                notas_5_str + ' e ' + notas_1_str)  
    elif notas_10_str != '':
            print(f'{valor_saque_str}{notas_50_str}, ' + 
                notas_5_str + ' e ' + notas_1_str)  
elif quantia_notas_diferentes == 4:
    if notas_100_str != '':
        if notas_50_str != '':
            print(f'{valor_saque_str}{notas_100_str}, ' + 
                notas_50_str + ', ' + notas_10_str + ' e ' + notas_5_str + notas_1_str)
        elif notas_10_str != '':
            print(f'{valor_saque_str}{notas_100_str}, ' + 
                notas_10_str + ', ' + notas_5_str + ' e ' + notas_1_str)            
    elif notas_50_str != '':
        if notas_10_str != '':
            print(f'{valor_saque_str}{notas_50_str}, ' + 
                notas_10_str + ', ' + notas_5_str + ' e ' + notas_1_str)      
elif quantia_notas_diferentes == 5:
            print(f'{valor_saque_str}{notas_100_str}, ' + 
                notas_50_str + ', ' + notas_10_str + ', ' + notas_5_str + ' e ' + notas_1_str)
