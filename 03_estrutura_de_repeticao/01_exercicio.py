while True:
   try:
       numero = int(input('Digite um valor de 0 a 10: '))
   except ValueError:
       print('Deve ser fornecido um valor inteiro')
   else:
       if 0 <= numero <= 10:
           print(f'Número informado é {numero}')
           break
       else:
           print('Número informado deve estar entre 0 e 10')
