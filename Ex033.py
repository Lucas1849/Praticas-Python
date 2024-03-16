#Faça um programa que leia três números e mostre qual é o maior e qual é menor

a = float(input('Digite um número:'))
b = float(input('Digite mais um número:'))
c = float(input('Digite outro número:'))

if a < b and a < c:
    print('O {:.2f} é o menor número'.format(a))
if b < a and b < c:
    print('O {:.2f} é o menor número'.format(b))
if c < b and c < a:
    print('O {:.2f} é o menor número'.format(c))

if a > b and a > c:
    print('O {:.2f} é o maior número'.format(a))
if b > a and b > c:
    print('O {:.2f} é o maior número'.format(b))
if c > a and c > b:
    print('O {:.2f} é o maior número'.format(c))