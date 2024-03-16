#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo slaário com 15% de aumento.

s = float(input('Qual é o salário do funcionário ?'))
a = s*0.15
print('O salário deste funcionário com 15% de aumento é {:.2f}'.format(s+a))
