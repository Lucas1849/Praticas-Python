#Crie um programa que leia um número real qualquer e mostre na tela a sua porção inteira 
import math

num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(num, math.trunc(num)))
