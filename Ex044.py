#Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento
# Á vista dinheiro/cheque: 10% de desconto
# Á vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

Produto = float(input('Qual o valor do produto ?'))
método = str('A opção de pagamento é ')

m1 = str('Á vista dinheiro/cheque')
m2 = str('Á vista no cartão')
m3 = str('Em até 2x no cartão')
m4 = str('3x ou mais no cartão')


print('''Escolha um método de pagamento:
[1] = 'Á vista dinheiro/cheque'
[2] = 'Á vista no cartão'
[3] = 'Em até 2x no cartão'
[4] = '3x ou mais no cartão'  ''')
opção = int(input('Sua opção:'))

if opção == 1:
    print('Você recebeu 10% de desconto, o preço do se produto agora é {:.2f}'.format(Produto - Produto*0.1))
elif opção == 2:
    print('Você recebeu 5% de desconto, o preço do seu produto agora é {:.2f}'.format(Produto - Produto*0.05))
elif opção == 3:
    print('Você não recebeu nenhum desconto, o preço do seu produto é {:.2f} e suas parcelas ficaram em 2 de R${:.2f}'.format(Produto, Produto/2))
elif opção == 4:
    parcelas =int(input('Quantas parcelas ?'))
    print('Você irá pagar 20% de juros ao mês,o preço final do seu produto é {:.2f} e suas parcelas ficaram em {} de R${:.2f}'.format(Produto + Produto *0.2, parcelas,(Produto/parcelas)+(Produto/parcelas)*0.2 ))
else:
    print('Escolha uma opção de pagamento válida')




