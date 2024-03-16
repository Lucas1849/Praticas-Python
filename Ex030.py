#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

N = int(input('Digite um número qualquer: '))
d = N%2

if d == 0:
    print('Esse número é par')
else:
    print('Esse número é ímpar')


