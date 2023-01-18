lista=[]
faturamento=0
while True:
    print('**Digite sair para encerrar**')
    produto=input('Entre com o nome do produto: ')
    if produto.lower() == 'sair':
        break
    quantidade=int(input('Entre com a quantidade do produto: '))
    if quantidade == -1:
        break
    preço=float(input('Entre com o preço do produto: '))
    if preço == -1:
        break
    registo=(produto,quantidade,preço)
    lista.append(registo)
for i in lista:
    faturamento = faturamento + (i[1] * i[2])
    print(f'Produto: {i[0]}, Quantidade:{i[1]}, Preço R$:{i[2]} O faturamento foi:{i[1]*i[2]}')
print(f'O faturamento total foi de R${faturamento:.2f}')