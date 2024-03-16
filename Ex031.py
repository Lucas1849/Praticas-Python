#Deseenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas

D = float(input('Qual a distância da sua viagem ?'))

if D <= 200:
    print('O valor da sua passagem será de R${}'.format(0.5 * D))
else:
    print('O valor da sua passagem será de R${}'.format(0.45 * D))