#Crie um programa que leia o nome e o preço de vários produtos.O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
soma = 0
count = 0
menor = 0
nome = 0
tot = 0
while True:
    produto = str(input('Digite o nome do produto: ')).title()
    preço = int(input('Digite o preço do produto: '))
    tot += 1
    #Total gasto na compra
    soma += preço

    #Quantos produtos custam mais de 1000
    if preço > 1000:
        count += 1
    
    #Produto mais barato
    if tot == 1:
        menor = preço
        nome = produto
    else:
        if preço < menor:
            menor = preço
            nome = produto
    confirm = str(input('Você quer continuar a cadastrar produtos [S = Sim] e [N = Não]? ')).upper().strip()[0]
    while confirm not in 'SsNn':
        confirm = str(input('Você quer continuar a cadastrar produtors [S = Sim] e [N = Não] ?')).upper().strip()[0]
    if confirm in 'Nn':
        break

print(f'O total gasto na sua compra é R${soma:.2f}')
print(f'Foram comprados {count} produtos quee custam mais de R$1000')
print(f'O {nome} é o produto mais barato que você comprou que custa R${menor}')
