'''
Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
Considere US$ 1,00 = R$ 4.79
'''
#CONVERSOR DE MOEDAS
M = int(input('Quanto reais você possui em sua carteira ? R$'))
#Dolar
print('Com R${} é possível comprar US${:.2F}'.format(M, M/4.79))
#Euro
print('Com R${} é possível comprar EUR{:.2F}'.format(M,M/5.39 ))