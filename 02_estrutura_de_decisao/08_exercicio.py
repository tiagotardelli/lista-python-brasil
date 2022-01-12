preco_produto_1 = float(input('Digite o valor do produto 1: '))
preco_produto_2 = float(input('Digite o valor do produto 2: '))
preco_produto_3 = float(input('Digite o valor do produto 3: '))
if preco_produto_2 > preco_produto_1 < preco_produto_3:
    print('Você deve comprar o produto 1, pois é o mais barato')
elif preco_produto_1 > preco_produto_2 < preco_produto_3:
    print('Você deve comprar o produto 2, pois é o mais barato')
else:
    print('Você deve comprar o produto 3, pois é o mais barato')
