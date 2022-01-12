ano = int(input('Digite um ano para saber se é bissexto ou não: '))
if (ano % 4) == 0:
    if (ano % 100) == 0:
        if (ano % 400) == 0:
            print(f"O ano {ano} é bissexto (tem 366 dias)")
        else:
            print(f"O ano {ano} não é um ano bissexto (tem 365 dias)")                
    else:
        print(f"O ano {ano} é bissexto (tem 366 dias)")
else:
    print(f"O ano {ano} não é um ano bissexto (tem 365 dias)")
