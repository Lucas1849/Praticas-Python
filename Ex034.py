#Faça um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# Para salários superiores a R$1250.00, calcule um aumento de 10%
# Para os valores inferiores ou iguals, o aumento ée de 15%

S = float(input('Qual o seu salário ?'))

if S > 1250:
    print('O seu aumento será de R${}, fazendo com que ganhe agora {}'.format(S * 0.10, S * 0.10 + S))
else:
    print('O seu aumento será de R${}, fazendo com que ganhe agora {}'.format(S * 0.15, S * 0.15 + S))