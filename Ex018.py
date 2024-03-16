'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo 
'''
import math

an = float((input('Digite um ângulo qualquer:')))
ra = math.radians(an)

print('O valor do seno de {} é {:.2f}'.format(an,(math.sin(ra))))
print('O valor do cosseno de {} é {:.2f}'.format(an, (math.cos(ra))))
print('O valor da tangente de {} é {:.2f}'.format(an, math.tan(ra)))
