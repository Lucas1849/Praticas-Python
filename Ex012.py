#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

p = float(input('Qual o preço do produto ? R$'))
d = p*0.05
print('O novo preço com os 5% de desconto da promoção do dia é {:.2f}'.format(p-d))
