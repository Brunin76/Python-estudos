"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = int(input('Entre com um número inteiro: '))
try:    
    if numero:
        print(f'Você digitou o número {numero}')
        if numero % 2==0:
            print('Par')
        else:
            print('Impar')
    else:
        print('Não digitou um número inteiro: ')
except:
    pass    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = float(input('Entre com a hora: '))
if hora >=00.00 and hora <=11.59:
    print('Bom dia!')
elif hora >=12.00 and hora <=17.59:
    print('Boa tarde!')
elif hora >=18.00 and hora <=23.59:
    print('Boa noite!')
else:
    print('nao sei')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

"""
nome = str(input('Entre com seu nome: '))
saber_nome = len(nome)
if saber_nome <= 4:
    print('Seu nome é curto ')
elif saber_nome >= 5 and saber_nome <=6:
    print('Nome ideal ')
else:
    print('Seu nome é muito grande')
