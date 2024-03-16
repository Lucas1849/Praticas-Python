# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7.00 por cada Km acima do limite

v = float(input('Qual a velocidade do veículo ?'))

if v > 80:
    print('Você está acima do limite de velocidade permitido, você precisa pagar uma multa de R${:.2f}'.format((v - 80)*7))
else:
    print('Você está dirigindo com segurança, tenha um bom dia!')
