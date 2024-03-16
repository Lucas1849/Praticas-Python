'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre  o comprimento
da hipotenusa
'''
'''
from math import pow
OP = float(input('Digite o comprimento do cateto oposto:'))
AD = float(input('Digite o comprimento do cateto adjacente:'))
HIP = pow(OP) + pow(AD)

print('O valor da hipotenusa desse triângulo retângulo é {}.'.format(HIP))

Como fiz primordialmente
'''
from math import hypot

OP = float(input('Digite o comprimento do cateto oposto:'))
AD = float(input('Digite o comprimento do cateto adjacente:'))
print('O valor da hipotenusa desse triângulo retângulo é {:.2f}.'.format(hypot(OP,AD)))